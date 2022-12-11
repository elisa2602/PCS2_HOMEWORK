from itertools import permutations
from math import factorial

n = int(input())
lst = []

for i in range(0,n):
    i += 1
    lst.append(i)

perm = list(permutations(lst))

nb_perm = factorial(n)
print(nb_perm)
lst_2 = []
for j in perm:
    print(*j)