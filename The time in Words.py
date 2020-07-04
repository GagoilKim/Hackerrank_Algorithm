#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the timeInWords function below.
def timeInWords(h, m):
    words = ["zero", "one", "two", "three", "four", 
            "five", "six", "seven", "eight", "nine", 
            "ten", "eleven", "twelve", "thirteen", 
            "fourteen", "fifteen", "sixteen",  
            "seventeen", "eighteen", "nineteen",  
            "twenty", "twenty one", "twenty two",  
            "twenty three", "twenty four",  
            "twenty five", "twenty six", "twenty seven", 
            "twenty eight", "twenty nine"]
    front = ''
    if m == 1:
        last = "one minute past " + words[h]
    elif m == 0:
        front += " o' clock"
        last = words[h] + front
    elif m == 15:
        front += "quarter past "
        last = front + words[h]
    elif m == 30:
        front += "half past "
        last = front + words[h]
    elif m == 45:
        front += "quarter to "
        last = front + words[h+1]
    elif m < 30:
        last = words[m] + " minutes past " + words[h] 
       
    # m > 30
    else:
        m = 60 - m
        last = words[m] + " minutes to " + words[h + 1]
    return last

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
