#!/usr/bin/env python3

def array_of_names(library):
    first = True
    str1 = "["
    for key, value in library.items() :
        if first == False :
            str1 += ", " 
        str1 += f"'{key.capitalize()} {value.capitalize()}'"
        first = False
    str1 += "]"
    return str1

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))