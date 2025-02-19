class Employee:
    language = "Python" # Class Attribute
    salary = 1600000

    def __init__(self, name, language, salary): # Dunder Method which is automatically called
        self.name = name
        self.language = language
        self.salary = salary
        print("I m on object which is automatically called")

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    def greet(self):
        print("Good Morning")

# ankit = Employee()

ankit = Employee("Ankit", 1500000, "Javascript")

ankit.name = "Ankit"
print(ankit.name, ankit.language, ankit.salary)
