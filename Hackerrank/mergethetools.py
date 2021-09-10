def merge_the_tools(string, k):
    len_t1 = int(k)
    len_s = len(string)
    i = 0
    for i in range(0, len(string), k):
        u_first = string[i: i + len_t1]
        u_final = ''
        for j in u_first: 
            if j in u_final:
                continue
            else:
                u_final += j
        print (u_final)
    return

string, k = input(), int(input())
merge_the_tools(string, k)