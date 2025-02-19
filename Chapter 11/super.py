class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a = 1

class Programmer(Employee):
    def __init__(self):
        print("Constructor of Programmer")
    b = 2

class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of Manager")
    c = 3

o = Employee()
print(o.a) # Prints the a attribute

o = Programmer()
print(o.a, o.b)

o = Manager()
print(o.a, o.b, o.c)

# super() method -> super() method is used to access the methods of a super class in the derived class.
# super().__init__()
# __init__() Calls constructor of the base class
