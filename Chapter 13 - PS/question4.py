# Write a program to filter a list of numbers which are divisible by 5.

def divisibleBy5(n):
    if (n % 5 == 0):
        return True
    return False

a = [12, 35, 56, 345, 1000, 72, 457, 3545, 38]

f = list(filter(divisibleBy5, a))
print(f)
