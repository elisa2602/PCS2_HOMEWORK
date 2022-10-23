from itertools import combinations_with_replacement

S, n = map(str, input().split())

S = sorted(S)
n = int(n)

for i in list(combinations_with_replacement(S,n)):
    print(*i, sep='')