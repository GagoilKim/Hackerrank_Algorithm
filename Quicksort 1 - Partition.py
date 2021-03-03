#!/bin/python3
import math
import os
import random
import re
import sys
# Complete the quickSort function below.
def quickSort(arr):
    p = arr[0]
    left = []
    right = []
    equal = [p]
    for i in range(1, len(arr)):
        if arr[i] > p:
            right.append(arr[i])
        elif arr[i] == p:
            equal.append(arr[i])
        else:
            left.append(arr[i])
    arr = left + equal + right
    return arr
    # print(' '.join(map(str, result))) 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    result = quickSort(arr)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()