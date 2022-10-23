from collections import namedtuple

N = int(input())
listy = []

for i in range(N+1):
    if i == 0:
        h = input()
        stud = namedtuple('Students', h)
    else:
        student = input().split()
        listy.append(stud(student[0],student[1],student[2], student[3]))
        
sum = 0
for j in listy:
    sum += int(j.MARKS)
    
print(sum/N)