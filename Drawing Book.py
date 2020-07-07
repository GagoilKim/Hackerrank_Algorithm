#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    post = abs(1-p)
    last = abs(n-p)
    result = 0
    # counting from last is better
    if post - last > 0 :
        tmp = n - p
        if tmp % 2 == 1:
            tmp -= 1
            result = tmp / 2
        else:
            result = tmp / 2
    # counting from begining is better
    else:
        # if p is odd
        if p % 2 == 1:
            p = p - 1
            result = p / 2
        else:
            result = p / 2
    print(int(result))
    return int(result)
    #
    # Write your code here.
    #

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
