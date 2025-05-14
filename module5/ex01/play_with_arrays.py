#!/usr/bin/env python3

array = [2, 8, 9, 48, 8, 22, -12, 2]
array2 = []
i = 0

while (i < len(array)) :
    array2.append(array[i] + 2)
    i = i + 1

print("Original array:", array)
print("New array:", array2)