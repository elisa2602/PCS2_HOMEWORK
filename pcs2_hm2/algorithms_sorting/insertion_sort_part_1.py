
import math
import os
import random
import re
import sys

def insertionSort1(n, arr):
    
    a = arr[n-1]
    b = n-2
    while b >= 0 and a < arr[b]:
        arr[b+1] = arr[b]
        stringy = str(arr)[1:-1].replace(",","")
        print(stringy)
        b -= 1
    arr[b+1] = a
    stringy = str(arr)[1:-1].replace(",","")
    print(stringy)
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
