#!/bin/python3
import math
import os
import random
import re
import sys
# Complete the utopianTree function below.
def utopianTree(n):
    cycle = 0
    result = 1
    for i in range(0, n):
        if cycle == 2:
            result = result * 2
            cycle = 1
        else:
            result += 1
            cycle += 1
    return (result)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        n = int(input())
        result = utopianTree(n)
        fptr.write(str(result) + '\n')
    fptr.close()