#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the surfaceArea function below.
def surfaceArea(A):
    # bottom & top
    botandtop = (len(A) * len(A[0])) * 2

    # front & back
    frontback = 0
    for i in range(len(A)):
        prev = A[i][0]
        frontback += prev
        for j in range(0, len(A[i])):
            if A[i][j] > prev:
               frontback +=  A[i][j] - prev
            prev = A[i][j]
    
    # sides
    sides = 0
    for j in range(len(A[0])):
        prev = A[0][j]
        sides += prev
        for i in range(len(A)):
            if A[i][j] > prev:
                sides += A[i][j] - prev
            prev = A[i][j]


    total = (botandtop + frontback * 2 + sides * 2)
    print(total)
    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    HW = input().split()

    H = int(HW[0])

    W = int(HW[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()
