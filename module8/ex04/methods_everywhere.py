#!/usr/bin/env python3
import sys

def  shrink(str2) :
    print(str2[:8])

def enlarge(str2) :
    leng = len(str2)
    while (leng < 8) :
        str2 = str2+"z"
        leng = len(str2)
    return (str2)

argc = len(sys.argv) - 1
i = 1
if (argc < 1) :
    print("none")
else :
    while (i <= argc) :
        str2 = sys.argv[i]
        if len(str2) < 8 :
            str2 = enlarge(str2)
        shrink(str2)
        i += 1