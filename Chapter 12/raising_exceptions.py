a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if (b == 0):
    raise ZeroDivisionError("Division by zero is not possible.")

else:
    print(f"The division of a/b is {a / b}")

# We can raise custom exceptions using the 'raise' keyword in python.
