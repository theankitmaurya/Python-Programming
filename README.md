# Python Programming Guide

## Introduction
Python is a high-level, interpreted programming language known for its readability and versatility. It is widely used in web development, data science, automation, and more.

## Installation
Download and install Python from the [official website](https://www.python.org/).

Check if Python is installed:
```sh
python --version
```

## Syntax Basics
### Printing Output
```python
print("Hello, World!")
```

### Variables and Data Types
```python
x = 10         # Integer
y = 3.14       # Float
name = "Alice" # String
is_valid = True # Boolean
```

### Comments
```python
# This is a single-line comment
"""
This is a 
multi-line comment
"""
```

## Control Flow
### Conditional Statements
```python
x = 10
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is 5")
else:
    print("x is less than 5")
```

### Loops
#### For Loop
```python
for i in range(5):
    print(i)
```

#### While Loop
```python
x = 0
while x < 5:
    print(x)
    x += 1
```

## Functions
```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))
```

## Data Structures
### Lists
```python
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits[0])  # Output: apple
```

### Dictionaries
```python
person = {"name": "Alice", "age": 25}
print(person["name"])  # Output: Alice
```

## File Handling
```python
with open("example.txt", "w") as file:
    file.write("Hello, Python!")
```

## Exception Handling
```python
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

## Object-Oriented Programming (OOP)
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

person1 = Person("Alice", 25)
print(person1.greet())
```

## Modules and Libraries
### Importing a Module
```python
import math
print(math.sqrt(16))  # Output: 4.0
```

### Using External Libraries
```python
# Install a package
pip install requests

# Example usage
import requests
response = requests.get("https://api.github.com")
print(response.status_code)
```

## Conclusion
Python is a powerful language with many applications. Keep exploring and building projects to enhance your skills!
