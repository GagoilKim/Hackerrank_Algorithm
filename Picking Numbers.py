#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    a = sorted(a)
    count = 0
    dic = {}
    for i in range(len(a)):
        if a[i]  in dic:
            dic[a[i]] +=1
        else:
            dic[a[i]] =1
    prev = -2
    for j in dic:
        print(dic[j])
        if j - prev ==1 :
            tmp = dic[j] + dic[prev]
            if tmp > count:
                count = tmp
        else:
            prev = j
            if dic[j] > count:
                count = dic[j]
    if len(dic) == 1:
        for j in dic:

            return dic[j]
    if prev == -2:
        return 0
    else:

        return count
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
