#!/bin/python3

import math
import os
import random
import re
import sys
import collections

# Complete the repeatedString function below.
def repeatedString(s, n):
    multiply = (n/len(s))+1
    nString = (multiply * s)[:n]
    counter = collections.Counter(nString) 
    return counter['a']


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
