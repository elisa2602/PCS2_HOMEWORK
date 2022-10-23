from itertools import permutations

S,k = map(str, input().split())

S = sorted(S)
k = int(k)

for i in list(permutations(S,k)):
    print(*i, sep = '')