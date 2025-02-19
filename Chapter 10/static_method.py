class Employee:
    language = "Python" # Class Attribute
    salary = 1600000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod # By marking the below function as static method it doesn't take self as parameter
    def greet():
        print("Good Morning")

ankit = Employee()
ankit.language = "Javascript" # Instance Attribute

# Below two will give the same output
ankit.greet()
ankit.getInfo()
Employee.getInfo(ankit)
