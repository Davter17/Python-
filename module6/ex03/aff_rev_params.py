#!/usr/bin/env python3
import sys

argc = len(sys.argv) - 1
if (argc == 0) :
    print("none")
else :
    while argc > 0 :
        print(sys.argv[argc])
        argc = argc - 1