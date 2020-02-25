#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
# Solution to https://www.hackerrank.com/challenges/2d-array/problem

def hourglassSum(arr):
    sums = []
    for x in list(range(4)):
        for y in list(range(4)):
            center = arr[x+1][y+1]; 
            up = arr[x][y+1];  upL = arr[x][y]; upR = arr[x][y+2]; 
            down = arr[x+2][y+1]; dowL = arr[x+2][y]; downR = arr[x+2][y+2]; 
            sums.append(center+up+upL+upR+down+dowL+downR)
    return max(sums)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)
    print(result)

    fptr.write(str(result) + '\n')

    fptr.close()
