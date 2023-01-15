from math import factorial

def perfmatch(file):
    code = ""
    with open(file, "r") as f:
        f.readline()
        for line in f:
            code += line.strip()
            
    numA = code.count("A")
    numC = code.count("C")
    res = factorial(numA)*factorial(numC)

    with open("resultpmch.txt", "w") as f:
        f.write(str(res))


perfmatch('rosalind_pmch.txt')