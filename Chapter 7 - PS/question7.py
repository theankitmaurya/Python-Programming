# Write a program to print the following star pattern.
#   *
#  ***
# ***** for n = 3

n = int(input("Enter the number: "))

for i in range(1, n + 1):
    print(" " * (n - i), end = "")
    print("*" * (2 * i - 1), end = "")
    print("")

# If we use end="" in print statement then it doesn't give a new line by default. end="" is an argument used in print function.
