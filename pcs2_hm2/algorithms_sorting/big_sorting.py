
import math
import os
import random
import re
import sys

def bigSorting(unsorted):
    
    for i in range (1,len(unsorted)):
        key = int(unsorted[i])
        j = i-1
        while j >= 0 and key < int(unsorted[j]):
            unsorted[j+1] =unsorted[j]
            j -= 1
        unsorted[j+1] = str(key)
    return unsorted

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    unsorted = []

    for _ in range(n):
        unsorted_item = input()
        unsorted.append(unsorted_item)

    result = bigSorting(unsorted)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
