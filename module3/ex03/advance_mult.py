#!/usr/bin/env python3

i = 0
j = 0

while i < 11 :
    j = 0
    print("Table of " + str(i), end =": ")
    while (j < 11) :
        print(i * j, end = " ")
        j = j + 1
    print()
    i = i + 1