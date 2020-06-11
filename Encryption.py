#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    l = math.sqrt(len(s))
    print(len(s))
    if l.is_integer():
        row = int(l)    
        column = int(l) 
        
    else:
        print(1)
        row = int(l)
        column = int(l)+1
    result = [[]*row for _ in range(column)]
    lists = list(s)
    while(len(lists) != 0):
        for c in range(len(result)):
            if not lists:
                break
            else:
                result[c] += (lists.pop(0))
    st = ""
    for i in range(len(result)):
        st+= " "
        for j in range(len(result[i])):
            st+= result[i][j]

    st = st[1:]
    return str(st)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
