#!/usr/bin/env python3

print("Enter the first number:")
num1 = int(input())
print("Enter the second number:")
num2 = int(input())
result = num1 * num2
print(num1, "x", num2, "=", result)
if result < 0 :
    print("The result is negative.\n")
elif result > 0 : 
    print("The result is positive.\n")
else :
    print("The result is both positive and negative.\n")