import math
import os
import random
import re
import sys

def timeConversion(s):
    
    hours = s[0:2]
    minutes = s[3:5]
    seconds = s[6:8]

    merid = s[8:10]

    if hours != '12' and merid == 'PM':
        time = int(hours) + 12
        print(f"{time}:{minutes}:{seconds}")

    elif hours == '12' and merid == 'PM':
        print(f"{hours}:{minutes}:{seconds}")

    elif hours == '12' and merid == 'AM':
        print(f"00:{minutes}:{seconds}")

    elif merid == 'AM':
        print(f"{hours}:{minutes}:{seconds}")


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
