import itertools

n = 2
nucleotides = 'A B C D E F G H I J'

lst = list(map(str,nucleotides.split()))
x = list(itertools.product(lst, repeat=n))

print(*[''.join(i) for i in x],sep='\n')