# Write a program to print multiplication table of a given number using for loop.

n = int(input("Enter for which you want to generate the table: "))

# 1st method
for i in range(1, 11):
    table = n * i
    print(table)

# 2nd method
for i in range(1, 11):
    print(f"{n} X {i} = {n * i}")
