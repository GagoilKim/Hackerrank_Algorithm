#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    count = 0
    pointer = 0
    length = len(c)
    while pointer != length:
        if pointer +2 < length:
            if c[pointer +2] == 0:
                pointer += 2
                count += 1
            else:
                pointer += 1
                count += 1
        else:
            pointer += 1
            count += 1
    return count-1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
