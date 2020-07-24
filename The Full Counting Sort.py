#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSort function below.
def countSort(arr):
    half = int(len(arr)/2)
    resultlist = []

    # check the list size
    maximum = 0
    for i in range(len(arr)):
        tmp = int(arr[i][0])
        if tmp > maximum:
            maximum = tmp
    
    resultlist = [[] for _ in range(maximum + 1)]
    result = ''
    # insert '-'
    for i in range(half):
        idx = int(arr[i][0])
        resultlist[idx].append('-')

    # insert words
    for i in range(half, len(arr)):
        idx = int(arr[i][0])
        word = arr[i][1]
        resultlist[idx].append(word)

    for i in range(len(resultlist)):
        for j in range(len(resultlist[i])):
            result += resultlist[i][j] + ' '
            

    print(result)

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
