from itertools import combinations

S, k = map(str, input().split())

S = sorted(S)
k = int(k)

for i in range(1, int(k)+1):
    lex = ["".join(sorted(i)) for i in combinations(S, i)]
    lex.sort()
    print("\n".join(lex))