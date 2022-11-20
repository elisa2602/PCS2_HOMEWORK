a = [5,1,6,2,4,3]

for count in range(0,len(a)):
    f = False
    for counter in range(0,len(a)-count-1):
        if a[counter] > a[counter + 1]:
            temp_value = a[counter]
            a[counter] = a[counter + 1]
            a[counter + 1] = temp_value
            f = True
    if f == False:
        break
print(a)

a= [5,2,4,6,1,3,2,  6]