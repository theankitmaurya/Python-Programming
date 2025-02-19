# Create a class "Programmer" for storing information of few programmers working at Microsoft.

class Programmer:
    company = "Microsoft"

    def __init__(self, name, salary, pincode):
        self.name = name
        self.salary = salary
        self.pincode = pincode

p = Programmer("Ankit", 1600000, 254371)
print(p.name, p.company, p.salary, p.pincode)
