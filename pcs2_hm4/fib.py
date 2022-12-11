n = int(input()) #nb of months
k = int(input()) #nb of rabbits pair produced by a pair
adults = 1
children = 1

for i in range(1,n-1):
    new_adults = adults + children*k
    children = adults
    adults = new_adults
print(adults)