#!/usr/bin/env python3
import sys

argc = len(sys.argv) - 1
i = 1
if (argc < 1) :
    print("none")
else :
    i = 1
    while i <= argc :
        match sys.argv[i].endswith("ism") :
            case True :
                i += 1
            case False :
                print(f"{sys.argv[i]}ism")
                i += 1