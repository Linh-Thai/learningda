#!/home/quyennx4/anaconda3/bin/python3
import pandas as pd
from pprint import pprint
from datetime import datetime

import traceback
import yaml
from yaml import CLoader as Loader

import re

import mysql.connector as conn
from sqlalchemy import create_engine


def print_runtime():
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("-"*19)


def extract_question_answer(quiz, answers):
    # quiz = row["quiz"]
    # answers = row["answers"]
    quiz_fmt = 0
    regex = re.compile(
        "\"(\d{1,9})\":\{\"id\":\"(\d{1,9})\",\"excerpt.*?\"answer\":\{(.*?)\},\"true\":\[\"([a-z]{4})"
    )
    regex_ans = re.compile("\"(\d{1,9})\":\[\"([a-z]{4})\"")
    if quiz[0] == "[" and quiz[-1] == "]":
        regex = re.compile(
            "\{\"id\":\"(\d{1,9})\",\"excerpt.*?\"answer\":\{(.*?)\},\"true\":\[\"([a-z]{4})"
        )
        regex_ans = re.compile("\"([a-z]{4})\"")
        quiz_fmt = 1
    ls_match = sorted(regex.findall(quiz), key=lambda tup: int(tup[0]))
    ls_ans = regex_ans.findall(answers)
    if quiz_fmt == 0:
        ls_ans = sorted(ls_ans, key=lambda tup: int(tup[0]))
    if len(ls_ans) == 0:
        ls_ans = [""] * len(ls_match)

    ls_output = []
    for match, ans in zip(ls_match, ls_ans):
        # print(match, ans, match[0]==ans[0])
        if quiz_fmt == 0:  # Full quiz
            # Match_id, question_id, choice, correct_ans, ans, correct
            if ans == "":  # Empty ans
                quiz_ans = (match[0], match[1], match[2], match[3], "", 0)
            elif match[0] == ans[0]:  # Full ans
                # Match_id, question_id, choice, correct_ans, ans, correct
                quiz_ans = (match[0], match[1], match[2], match[3], ans[1],
                            int(match[3]==ans[1]))
        else:  # List of question_id, no match_id
            # Match_id=-1, question_id, choice, correct_ans, ans, correct
            if ans == "":  # Empty ans
                quiz_ans = (-1, match[0], match[1], match[2], "No answer", 0)
            else:  # ans as list of choices, no index
                quiz_ans = (-1, match[0], match[1], match[2], ans,
                            int(match[2]==ans))

        ls_output.append(quiz_ans)
    # if len(ls_output) != len(ls_match):
    #     return []
    return ls_output


def split_choice(ch):
    regex_split_choice = re.compile("\"([a-z]{4})\"")
    return regex_split_choice.findall(str(ch))


def decode_answer(list_choice, ans):
    if not isinstance(ans, str) or len(ans) != 4:
        return "error"
    idx = -1
    try:
        idx = list_choice.index(ans)
    except ValueError:
        return "error"

    return "ABCDEFGH"[idx]


if __name__ == "__main__":
    # Read params from yml file
    with open("mysql_conn.yaml", "r") as f:
        conf = yaml.load(f, Loader=Loader)
    host = conf["mysql"]["host"]
    port = conf["mysql"]["port"]
    db_name = conf["mysql"]["db_name"]
    user = conf["mysql"]["user"]
    pwd = conf["mysql"]["pwd"]
    if pwd is None:
        pwd = ""
    print(host, db_name, user, pwd)
    print("# Split table into smaller parts")
    table_name = "quiz_result_history"
    try:
        db_conn = conn.connect(host=host, database=db_name, port=port,
                               user=user, passwd=pwd, use_pure=True)
        query = f"SELECT MAX(result_id) AS max_id FROM {table_name};"
        pdf_max_id = pd.read_sql(query, db_conn)
        db_conn.close()
    except:
        traceback.print_exc()
        db_conn.close()
    max_id = pdf_max_id["max_id"][0]
    print(f"# max_id: {max_id}")
    interval = 4000
    ls_chunk = [[i*interval, min((i+1)*interval-1, max_id)]
                for i in range(max_id//interval+1)]
    pprint(ls_chunk)

    ls_result_hist = []
    print(f"# Format {table_name} by chunks")
    for start_id, end_id in ls_chunk:
        print("#", start_id, "-", end_id)
        table_name = "quiz_result_history"
        try:
            db_conn = conn.connect(host=host, database=db_name, user=user, passwd=pwd, port=port)
            query = f"SELECT * FROM {table_name} WHERE result_id >= {start_id} AND result_id <= {end_id};"
            pdf_history = pd.read_sql(query, db_conn)
            db_conn.close()
        except:
            traceback.print_exc()
            db_conn.close()

        pdf_history["quiz_ans"] = pdf_history.apply(
            lambda row: extract_question_answer(row["quiz"], row["answers"]),
            axis=1
        )  # ["quiz"], row["answers"]))

        pdf_history_short = pdf_history[[
            "result_id", "essay", "quiz_ans"
        ]].copy()

        pdf_01 = pdf_history_short.explode(column="quiz_ans").reset_index()
        ls_match_col = ["match_id", "question_id", "choice", "correct_ans", "ans", "correct"]
        pdf_02 = pd.DataFrame(pdf_01["quiz_ans"].tolist(), index=pdf_01.index, columns=ls_match_col)
        pdf_02["list_choice"] = pdf_02["choice"].apply(split_choice)
        pdf_03 = pd.merge(pdf_01, pdf_02, left_index=True, right_index=True)
        print(f"pdf_01: {pdf_01.shape}; pdf_02: {pdf_02.shape}; pdf_03: {pdf_03.shape}; ")

        ls_result_hist.append(
            pdf_03[["result_id", "question_id", "list_choice", "correct_ans", "ans"]]
            .copy())
        print_runtime()

    o_path = "quiz_result_history_1.pkl"
    print(f"Write to: {o_path}")
    pdf_result_hist = pd.concat(ls_result_hist).reset_index()
    pdf_result_hist.to_pickle(o_path, compression="bz2")
    pdf_result_hist["decode_result"] = pdf_result_hist.apply(
        lambda x: decode_answer(x["list_choice"], x["correct_ans"]), axis=1)
    pdf_result_hist["decode_ans"] = pdf_result_hist.apply(
        lambda x: decode_answer(x["list_choice"], x["ans"]), axis=1)

    print("# Write to db")
    ls_output_col = ["result_id", "question_id", "decode_result", "decode_ans"]
    try:
        conn_str = f"mysql+pymysql://{user}:{pwd}@{host}:{port}/{db_name}"
        engine = create_engine(conn_str)
        pdf_result_hist[ls_output_col].to_sql(
            "quiz_result_history_1", con=engine,
            if_exists="replace", chunksize=1000, index=False)
    except:
        traceback.print_exc()
