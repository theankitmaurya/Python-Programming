# Write a python function which converts inches to cms.

n = int(input("Enter value in inches: "))
def inch_to_cms(inch):
    value = inch * 2.54
    return value

print(f"The corresponding value in cms is {inch_to_cms(n)}")
