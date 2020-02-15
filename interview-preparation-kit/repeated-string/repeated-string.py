#!/bin/python3

import math
import os
import random
import re
import sys
import collections

# Complete the repeatedString function below.
def repeatedString(s, n):
    totCount = centinel =0
    while centinel<n:
        for character in s:
            centinel+=1
            if character == 'a':
                totCount+=1
            if centinel == n:
                break
    print(totCount)
    return totCount


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
