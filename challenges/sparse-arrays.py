#!/bin/python3

import math
import os
import random
import re
import sys
import collections

# Complete the matchingStrings function below.
# Solution to  https://www.hackerrank.com/challenges/sparse-arrays/problem
def matchingStrings(strings, queries):
    counter = collections.Counter(strings)
    result = []
    for q in queries:
        print(q)
        instances=(counter[q])
        result.append(instances)
    print(result)
    return result

    


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    #fptr.write('\n'.join(map(str, res)))
    #fptr.write('\n')

    #fptr.close()
