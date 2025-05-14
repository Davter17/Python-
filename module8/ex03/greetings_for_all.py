#!/usr/bin/env python3

def greetings(char=None) :
    if char is None :
        print("Hello, noble stranger")
    elif type(char) == str :
        print(f"Hello, {char}.")
    else :
        print("Error! It was not  a name.")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)