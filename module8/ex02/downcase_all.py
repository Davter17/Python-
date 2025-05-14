#!/usr/bin/env python3
import sys

def downcase_it(char) :
    return char.lower()

argc = len(sys.argv) - 1
i = 1
if (argc == 0) :
    print("none")
while (i <= argc) :
    print(downcase_it(sys.argv[i]))
    i += 1
