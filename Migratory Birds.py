#!/bin/python3

import math
import os
import random
import re
import sys
import operator

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    t = {1:0, 2:0, 3:0, 4:0, 5:0}
    for i in arr:
        t[i] += 1
    return max(t, key = t.get)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
