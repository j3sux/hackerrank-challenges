#!/bin/python3

import math
import os
import random
import re
import sys

res = []
# Complete the arrayManipulation function below.
# Solve https://www.hackerrank.com/challenges/crush/
def arrayManipulation(n, queries):
    res = [0 for x in range( n )]

    for e in queries:
        for i in range(e[0],e[1]+1):
            res[i-1] = res[i-1] + e[2]        
    return max(res)
        


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    queries = []
    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))
    result = arrayManipulation(n, queries)
    #fptr.write(str(result) + '\n')
    #fptr.close()
