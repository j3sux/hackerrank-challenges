#!/bin/python3

import math
import os
import random
import re
import sys
import collections

# Complete the repeatedString function below.
# Solution to https://www.hackerrank.com/challenges/repeated-string/problem
def repeatedString(s, n):
 
    multiple = (n//len(s))
    totCount = (s.count('a')*multiple) + s[:int(n - (len(s)*multiple))].count('a')
   
    return totCount  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
