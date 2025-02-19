class Employee:
    language = "py" #This is class attribute
    salary = "1600000"

ankit = Employee()
ankit.language = "Javascript" # This is instance attribute
print(ankit.language, ankit.salary)

# Note: Instance attributes, take preference over class attributes during assignment & retrieval.

# When looking up for ankit.attribute it checks for the following:
# 1) Is attributes present in object?
# 2) Is attributes present in class?
