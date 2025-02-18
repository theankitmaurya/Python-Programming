# Write a python program using function to convert Celsius to Fahrenheit and vice versa.

# Formula -> C = 5 * (F - 32) / 9

def celsius_to_fahrenheit():
    f = int(input("Enter temperature in fahrenheit: "))
    c = 5 * (f - 32) / 9
    print(f"{round(c, 2)}°C")
    
celsius_to_fahrenheit()

# Formula -> (9 * C) / 5 + 32

def fahrenheit_to_celsius():
    c = int(input("Enter temperature in celsius: "))
    f = (9 * c) / 5 + 32
    print(f"{round(f, 2)}°F")

fahrenheit_to_celsius()
