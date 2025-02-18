# factorial(1) = 1
# factorial(2) = 2 X 1
# factorial(3) = 3 X 2 X 1
# factorial(4) = 4 X 3 X 2 X 1
# factorial(5) = 5 X 4 X 3 X 2 X 1

# factorial(n) = n X n - 1 X ... X 3 X 2 X 1

# factorial(n) = n * factorial(n - 1)

def factorial(n):
    if(n == 1 or n == 0):
        return 1
    return n * factorial(n - 1)

n = int(input("Enter a number: "))
print(f"The factorial of {n} is: {factorial(n)}")

# This is a best example of recursion.
# The programmer needs to be extremely careful while working with recursion to ensure that the function doesn't infinitely calling itself.
# Recursion is sometimes the most direct way to code an algorithm.
