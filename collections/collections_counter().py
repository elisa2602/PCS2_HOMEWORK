from collections import Counter

X = input()
size_list = Counter(map(int, input().split()))
n = input()
N = int(n)
earn = 0

for customer in range(N):
    size, xi = map(int, input().split())
    if size in size_list and size_list[size] > 0:
        size_list[size] -= 1
        earn += xi
    
print(earn)