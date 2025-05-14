#!/usr/bin/env python3

array = [2, 8, 9, 48, 8, 22, -12, 2]
array2 = []
i = 0

# while (i < len(array)) :
#     if array[i] > 5 :
#         array2.append(array[i] + 2)
#     i = i + 1
# array2 = set(array2)

while (i < len(array)) :
    if array[i] > 5 :
        #if array[i] not in array2:
        #    array2.append(array[i] + 2)
        j = 0
        new = True
        while (j < len(array2)) :
            if (array[i] + 2 == array2[j]) :
                new = False
            j += 1
        if new == True :
            array2.append(array[i] + 2)
    i = i + 1

print(array)
print("{", end="")
j=0
first = True
while (j < len(array2)) :
    if first == False :
        print(", ", end="")
    first = False
    print(array2[j], end="")
    j+=1
print("}")
