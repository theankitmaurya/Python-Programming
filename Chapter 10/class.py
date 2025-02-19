class Employee:
    language = "py" #This is class attribute
    salary = "1600000"

ankit = Employee()
ankit.name = "Ankit" # This is instance attribute
print(ankit.name, ankit.language, ankit.salary)

# An object is an instantiation of a class. When class is defined, a template (info) is defined. Memory is allocated only after object instantiation.

# Objects of a given class invoke the methods available to it without revealing the implementation detailed to the user. - Abstractions and Encapsulation

# Modelling a problem in OOPS ->
# We identify the following in our problem:
# 1. Noun -> Class -> Employee
# 2. Adjective -> Attributes -> name, age, salary
# 3. Verbs -> Methods -> getSalary(), increment()


# Here, name is an instance attribute and salary and language are class attributes as they directly belong to the class.
