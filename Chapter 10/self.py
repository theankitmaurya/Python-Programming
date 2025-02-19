class Employee:
    language = "Python" # Class Attribute
    salary = 1600000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    def greet(self):
        print("Good Morning")

ankit = Employee()
ankit.language = "Javascript" # Instance Attribute

# Below two will give the same output
ankit.greet()
ankit.getInfo()
Employee.getInfo(ankit)
