if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    summy = 0
    average = float()
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    for i in student_marks[query_name]:
        summy += i
    average = summy / len(student_marks[query_name])
    print("%.2f" %average)
