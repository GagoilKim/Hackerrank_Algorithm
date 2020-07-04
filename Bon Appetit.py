#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    total = 0
    for i in range(len(bill)):
        total += bill[i]
    total -= bill[k]
    total = int(total / 2)
    if total == b:
        print('Bon Appetit')
    else:
        print(b - total)

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
