#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    tmp = str(s)
    if tmp[8:10] == "PM":
        tmp = tmp[0:8]
        comp = tmp[0] + tmp[1]
        front = int(tmp[0])
        back = int(tmp[1])
        if int(comp) < 12:
            
                front += 1
                back +=2
                tmp  = (str(front)+ str(back) +tmp[2:8])
                return tmp
            
        else:
            return tmp
    else:
        tmp = tmp[0:8]
        comp = tmp[0] + tmp[1]
        if int(comp) == 12:
            tmp  = ("00" +tmp[2:8])
            return tmp
        return tmp    
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
