# Write a program to find the maximum of the numbers in a list using the reduce function.

from functools import reduce

l = [25, 356, 78, 100, 343, 34, 40, 50, 65]

def greater(a, b):
    if (a > b):
        return a
    return b

print(reduce(greater, l))
