student_grade_lis = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    student_grade_lis.append([name, score])
sorted_scores = sorted(list(set([x[1] for x in student_grade_lis])))
second_grade = sorted_scores[1]
    
name_final_lis = []
for student in student_grade_lis:
    if second_grade == student[1]:
        name_final_lis.append(student[0])
        
for student in sorted(name_final_lis):
    print(student)