#!/bin/python3

import math
import os
import random
import re
import sys
import collections

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    totalPairs = 0
    counter = collections.Counter(ar)

    for color in counter:
        numColorSocks=(counter[color])   
        totalPairs += numColorSocks // 2

    return totalPairs
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()