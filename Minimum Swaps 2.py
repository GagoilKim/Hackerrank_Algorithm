#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    count = 0
    for i in range(len(arr)-1):
        m = i
        for j in range(i+1, len(arr)):
            if arr[m] > arr[j]:
                m = j 
        # swap
        if i != m:
            tmp = arr[i]
            arr[i] = arr[m]
            arr[m] = tmp
            count += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
