#!/usr/bin/env python3
import sys

argc = len(sys.argv) - 1
if (argc != 1) :
    print("none")
else :
    password = input("What was the parameter? ")
    if password == sys.argv[1] :
        print("Good job!")
    else :
        print("Nope, sorry...")