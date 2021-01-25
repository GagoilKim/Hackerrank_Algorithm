#!/bin/python3
import math
import os
import random
import re
import sys
# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    ar= sorted(ar)
    tmp = 0
    count = 0
    result = 0
    for i in range(len(ar)):
        if tmp == ar[i]:
            count += 1
            if count / 2 == 1:
                count = 0
                result += 1
        else:
            tmp = ar[i]
            count = 1 
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    fptr.write(str(result) + '\n')
    fptr.close()
