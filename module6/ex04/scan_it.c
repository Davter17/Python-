#!/usr/bin/env python3
import sys
import re

argc = len(sys.argv) - 1
if (argc != 2) :
    print("none")
else :
    array = re.findall(sys.argv[1], sys.argv[2])
    if (len(array) == 0) :
        print ("none")
    else :
        print(len(array))