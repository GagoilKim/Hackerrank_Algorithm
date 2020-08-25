#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the icecreamParlor function below.
def icecreamParlor(m, arr):
    tmp1 = 0
    tmp2 = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            add = arr[i] + arr[j]
            if add == m:
                tmp1 = i
                tmp2 = j
                break
    tmp1 += 1
    tmp2 += 1
    return tmp1, tmp2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        m = int(input())

        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
