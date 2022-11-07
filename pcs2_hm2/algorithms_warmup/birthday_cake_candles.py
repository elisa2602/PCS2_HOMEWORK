import math
import os
import random
import re
import sys

def birthdayCakeCandles(candles):
    a = 0
    temp_value = 0
    for i in range(1, len(candles)):
        if candles[i] > temp_value:
            temp_value = candles[i]

    for i in range(0, len(candles)):
        if candles[i] == temp_value:
            a = a+1
    
    return a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'])

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()