n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
total = 0
for i in student_marks[query_name]:
    total += i 
average = total / len(student_marks[query_name])
print('%.2f'%average)