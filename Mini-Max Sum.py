#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()
    total = 0

    for i in arr:
        total += i
    minValue = total - arr[4]
    maxValue = total - arr[0]
    print(str(minValue) + " " + str(maxValue))
    return minValue, maxValue

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
