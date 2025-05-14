#!/usr/bin/env python3

age = int(input("Please tell me your age: "))
print("You are currently " + str(age) + " years old.")
i = 10
while i < 31 :
    print("In", str(i), "years, you'll be", str(i + age), "years old.")
    i = i + 10