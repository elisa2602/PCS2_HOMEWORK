
import math
import os
import random
import re
import sys

def countingSort(arr):
   
    arr_count = [0]*100
    for i in arr:
        arr_count[i]+= 1
    final_arr = []
    for i in range(100):
        for j in range(arr_count[i]):
            final_arr.append(i)
    return final_arr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
