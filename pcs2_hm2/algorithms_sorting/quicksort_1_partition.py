
import math
import os
import random
import re
import sys

def quickSort(arr):

    i = 1
    for j in range(i, len(arr)):
        if arr[j] < arr[0]:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[0], arr[i-1] = arr[i-1], arr[0]
    return arr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
