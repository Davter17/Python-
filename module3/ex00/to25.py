#!/usr/bin/env python3

try:
    print("Enter a number less than 25")
    num = int(input())

    if num > 25 :
        print("Error")
    else : 
        while num <= 25 :
            print("Inside the loop, my variable is", num)
            num = num + 1
except :
    print("Write only integer numbers.")