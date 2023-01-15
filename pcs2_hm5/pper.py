from math import factorial, comb

def partpermscount(file):
    with open(file, "r") as f:
        line = f.readline().strip()
    
    n,k = line.split(" ")
    n,k = int(n), int(k)
    mod = 1000000
    res = comb(n,k)%mod*factorial(k)%mod
    with open("resultpper.txt", "w") as f:
        f.write(str(res))
    
    return res

partpermscount('rosalind_pper.txt')