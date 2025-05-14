#!/usr/bin/env python3
import sys

argc = len(sys.argv) - 1
i = 1
if (argc != 1) :
    print("none")
else :
    i = 0
    none = True
    while (i < len(sys.argv[1])) :
        if sys.argv[1][i] == 'z' :
            print('z', end="")
            none = False
        i += 1
    if (none == True) :
        print("none", end="")
    print()