import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    sum_d1 = 0
    sum_d2 = 0
    for i in range(0,len(arr)):
        sum_d1 += arr[i][i]
        reversy = len(arr)-i-1
        sum_d2 += arr[i][reversy]
    return abs(sum_d1-sum_d2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUTPATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()