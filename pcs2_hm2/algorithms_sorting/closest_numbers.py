import math
import os
import random
import re
import sys

def closestNumbers(arr):
    arr.sort()
    res = []
    mini = arr[1] -arr[0]

    for i in range(1,len(arr)):
        diff = arr[i] - arr[i-1]

        if diff == mini:
            res.extend([arr[i-1],arr[i]])
        elif diff < mini:
            mini = diff
            res = [arr[i-1],arr[i]]

    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str,result)))
    fptr.write('\n')

    fptr.close()