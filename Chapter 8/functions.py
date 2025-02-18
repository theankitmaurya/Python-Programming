# This can be very hectic to print the same thing for many times and to write its code is also increases. So to avoid this we use functions.
a = int(input("Enter your number: "))
b = int(input("Enter your number: "))
c = int(input("Enter your number: "))

average = (a + b + c) / 3
print(average)

# This is the format of defining functions in python which also reduces the number of lines of code written

# Function Definition
def avg():
    a = int(input("Enter your number: "))
    b = int(input("Enter your number: "))
    c = int(input("Enter your number: "))

    average = (a + b + c) / 3
    print(average)

avg() # Function Call

# Types Of Functions ->
# 1. Built in functions: Already present in python
# Example -> len(), print(), range() etc. are built in functions

# 2. User defined functions: Defined by the user
# Example -> avg(), func1(), sum() etc. ar user defined functions
