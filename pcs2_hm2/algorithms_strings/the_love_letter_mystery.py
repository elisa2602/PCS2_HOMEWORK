
import math
import os
import random
import re

def theLoveLetterMystery(s):

    a = s[::-1]
    b = 0
    for i in range(len(s)//2):
        b = b + abs(ord(s[i])- ord(a[i]))
    return b
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        fptr.write(str(result) + '\n')

    fptr.close()
