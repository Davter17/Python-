#!/usr/bin/env python3

#def find_the_redheads(library):
#    redheads = list(filter(lambda k: library[k] == "red", library.keys()))
#    return str(redheads)


def find_the_redheads(library) :
    first = True
    str1 = "["
    for key, value in library.items() :
        if value == "red" :
            if (first == False) :
                str1 += ", "
            str1 += f"'{key}'"
            first = False
    str1 += "]"
    return (str1)

dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

print(find_the_redheads(dupont_family))