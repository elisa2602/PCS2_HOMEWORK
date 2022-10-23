from collections import deque
N = int(input())
d = deque()
for i in range(N):
    a = input().split()
    if a[0] == "append":
        d.append(int(a[1]))
    elif a[0] == "pop":
        d.pop()
    elif a[0] == "popleft":
        d.popleft()
    elif a[0] == "appendleft":
        d.appendleft(int(a[1]))
print(' '.join(map(str, d)))