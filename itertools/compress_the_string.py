from itertools import groupby

listy = []
S = input()

for i, j in groupby(S):
    listy.append((len(list(j)), int(i)))
print(*listy)
