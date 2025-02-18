# Write a program using functions to find greatest of three numbers.

a = int(input("Enter your number: "))
b = int(input("Enter your number: "))
c = int(input("Enter your number: "))

def greatest_of_three_numbers(a, b, c):
    if(a > b and a > c):
        print("a is greater than b and c")
        print("Value of: ")
        return a
    elif(b > a and b > c):
        print("b is greater than a and c")
        print("Value of: ")
        return b
    elif(c > a and c > b):
        print("c is greater than a and b")
        print("Value of: ")
        return c

print(greatest_of_three_numbers(a, b, c))
