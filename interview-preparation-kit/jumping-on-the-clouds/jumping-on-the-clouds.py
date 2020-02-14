#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
# Solution to https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem
def jumpingOnClouds(c):
    lastCloud = len(c)-1
    position=numJumps=0
    while (position<lastCloud):
        bigJump=position+2
        smallJump=position+1
        if (bigJump<=lastCloud and c[bigJump]==0):
            position=bigJump
            numJumps+=1
        elif (smallJump<=lastCloud and c[smallJump]==0):
            position=smallJump
            numJumps+=1
    return numJumps    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
