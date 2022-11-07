
import math
import os
import random
import re
import sys

def insertionSort2(n, arr):

    for i in range(1,n):
        for j in range(i):
            if arr[j] > arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
        print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
