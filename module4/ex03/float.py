#!/usr/bin/env python3

decimal = float(input("Give me a number: "))
if decimal - int(decimal) == 0 :
    print("This number is an integer")
else :
    print("This number is a decimal")