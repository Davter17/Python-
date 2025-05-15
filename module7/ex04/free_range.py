#!/usr/bin/env python3
import sys

argc = len(sys.argv) - 1
i = 1
if (argc != 2) :
    print("none")
else :
    try:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
        if num1 > num2 :
            array = list(range(num1, num2 - 1, -1))
        else :
            array = list(range(num1, num2 + 1))
            
        print(array)
    except:
        print("Error")
