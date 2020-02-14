#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    level=valleys=0
    for action in s:
        prevLevel=level
        level = level+1 if action == 'U' else level-1 
        if level == 0 and prevLevel<0:
            valleys+=1
    return valleys      

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)
    
    fptr.write(str(result) + '\n')

    fptr.close()
