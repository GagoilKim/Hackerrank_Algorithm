#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    maxR = scores[0]
    minR = scores[0]
    countMax = 0
    countMin = 0
    for i in range(0, len(scores)):
        if scores[i] > maxR:
            maxR = scores[i]
            countMax += 1
        if scores[i] < minR:
            minR = scores[i]
            countMin += 1
    print(countMax)
    print(countMin)
    return countMax, countMin 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
