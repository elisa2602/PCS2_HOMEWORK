# k= homozygote dominant (AA)
# m = heterozygote (Aa)
# n = homozygote recessive (aa)

import random

k = int(input())
m = int(input())
n = int(input())
p = k + m + n

listy =[]
listy.append(k)
listy.append(m)
listy.append(n)
x = random.choice(listy)
y = random.choice(listy)

prob_k = k/p
prob_m = m/p
prob_n = n/p

tot = p-1

prob_phen_ev = prob_k + prob_m * ((k/tot) + (0.75*((m-1)/tot)) + (0.5*(n/tot))) + prob_n * ((k/tot) + (0.5 * (m/tot)))
print(prob_phen_ev)


