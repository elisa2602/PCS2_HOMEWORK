
import math
import os
import random
import re
import sys

def miniMaxSum(arr):
    arr.sort()
    min_n = 0
    max_n = 0
    
    i = 0
    while i < len(arr):
        min_n += arr[i]
        i += 1
        if i == 4:
            break
    
    i = len(arr)-1   
    while i >= 0:
        max_n += arr[i]
        i -= 1
        if i == len(arr)-5:
            break
        
    print(min_n, max_n)  
    
        
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
