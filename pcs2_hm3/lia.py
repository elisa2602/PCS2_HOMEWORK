import math  

A = int(input())                                                                          
B = int(input())                                                                          
P = 2**A                                                                       
count = 0  

for i in range(B, P + 1):                                                      
    prob = (math.factorial(P) / (math.factorial(i) * math.factorial(P - i))) * (0.25**i) * (0.75**(P - i))                                                        
    count += prob                                                        
print(count)        