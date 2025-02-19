class Employee: # Base Class
    company = "ITC"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

# We can use Programmer class by two types ->

# 1st type -> In this if we have to use Programmer class for many times then we have to change it manually in Employee class as well as in Programmer class too.
class Programmer:
    company = "ITC Infotech"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

    def showLanguage(self):
        print(f"The name is {self.name} and the he is good with {self.language} language")

# 2nd type -> In this if we have to use Programmer class for many times then we have to change only in Employee class as Employee class is given as a parameter in the Programmer class. After passing Employee as a parameter in Programmer class all of its attributes can be accessible by Programmer class. And by this we don't have to manually change in Programmer class too. We have to only change in Employee class and in Programmer class it gets updated.
class Programmer(Employee): # Derived or Child Class
    company = "ITC Infotech"

    def showLanguage(self):
        print(f"The name is {self.name} and the he is good with {self.language} language")


a = Employee()
b = Programmer()

print(a.company, b.company)

# Types of Inheritance ->
# 1. Single Inheritance -> Single Inheritance occurs when child class inherits only a single parent class.
# 2. Multiple Inheritance -> Multiple Inheritance occurs when the child class inherits from more than one parent classes.
# 3. Multilevel Inheritance -> When a child becomes a parent for another child class.
