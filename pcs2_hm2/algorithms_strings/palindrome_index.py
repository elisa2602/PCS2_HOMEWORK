
import math
import os
import random
import re
import sys

def palindromeIndex(s):
    
    rev_str = s[::-1]
    for i in range(0,len(s)):
        if s[i] != rev_str[i]:
            stringy = s[:i] + s[i+1:]
            if stringy == stringy[::-1]:
                return i
            else:
                return len(s)-1-i
    return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
