#!/usr/bin/env python3
import sys

argc = len(sys.argv) - 1
if (argc < 1) :
    print("none")
else :
    print(f"parameters: {argc}")
    for arg in sys.argv[1:] :
        print(f"{arg}:", len(arg))
    #i = 1
    #while (i <= argc) :
    #    print(f"{sys.argv[i]}:", len(sys.argv[i]))
    #    i = i + 1