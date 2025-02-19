class Employee:
    a = 1
    @classmethod
    def show(cls):
        print(f"the class attribute of a is {cls.a}")

e = Employee()
e.a = 45

e.show()

# Class Method -> A class method is a method which is bound to the class and not the object of the class.
# @classmethod decorator is used to create a class method.
# Syntax: @classmethod
#         def(cls, p1, p2):
