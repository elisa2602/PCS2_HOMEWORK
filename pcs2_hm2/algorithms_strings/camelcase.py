
import math
import os
import random
import re
import sys

def camelcase(s):

    a = 0
    for i in s:
        if i.isupper():
            a += 1
    return a + 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
