class Employee:
    a = 1

    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

e = Employee()
e.a = 45

e.name = "Ankit Maurya"
print(e.fname, e.lname)

e.show()

# Property Decorators -> If e = Employee() is an object of class employee, we can print(e.name) to print the ename by internally calling name() function.
# Consider the following class:
# class Employee:
#     @property
#     def name(self):
#         return self.ename

# @.Getters and @.Setters
# The method name with '@property' decorator is called getter method.
# We can define a function + @name.setter decorator like below:
# @name.setter
# def name (self, value):
#     self.ename = value
