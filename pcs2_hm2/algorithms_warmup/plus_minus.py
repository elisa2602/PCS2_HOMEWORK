import math
import os
import random
import re
import sys

def plusMinus(arr):
    pos = 0
    neg = 0
    zero = 0

    for i in range(len(arr)):
        if arr[i] > 0:
            pos += 1
        elif arr[i] == 0:
            zero += 1
        else:
            neg += 1
    print(pos/len(arr))
    print(neg/len(arr))
    print(zero/len(arr))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)