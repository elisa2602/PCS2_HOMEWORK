engl_stu = int(input())
engl_space = set(map(int, input().split()))
french_stu = int(input())
french_space = set(map(int, input().split()))

print(len(engl_space.union(french_space)))