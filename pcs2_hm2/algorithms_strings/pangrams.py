
import math
import os
import random
import re
import sys

def pangrams(s):

    low_str = s.lower()
    ascii_arr = []
    for i in range(len(low_str)):
        ascii_arr.append(ord(low_str[i]))
    for i in range(97, 123): 
        if i not in ascii_arr:
            return "not pangram"
    return "pangram"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
