n = int(input()) #n-th month
m = int(input()) #nb of months that the rabbits live
life = [0] * m
life[0] = 1

#range(start, stop, step)
for i in range(n-1):
    count = 0
    for j in range(m-1,0,-1):
        count = count + life[j]
        life[j] = life[j-1]
    life[0] = count

print(sum(life))
