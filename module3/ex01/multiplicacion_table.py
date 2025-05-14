#!/usr/bin/env python3

try:
    print("Enter a number")
    num = int(input())

    i = 0
    while i < 10 :
        print(i, "x", num, "=", num * i)
        i = i + 1
except :
    print("Write only integer numbers.")