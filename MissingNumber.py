#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the missingNumbers function below.
def missingNumbers(arr, brr):
    for i in arr:
        if i in brr:
            brr.remove(i)
    brr.sort()
    tmp = brr[0]
    for i in range(1, len(brr)):
        if tmp == brr[i]:
            brr.remove(i)
        else:
            tmp = brr[i]
    print(brr)
    return brr


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
