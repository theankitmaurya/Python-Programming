# Add a static method in problem 2, to greet the user with hello.

enter = int(input("Enter the number: "))

class Calculator:

    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"1. The square is {self.n * self.n}")

    def cube(self):
        print(f"2. The cube is {self.n * self.n * self.n}")

    def square_root(self):
        print(f"3. The square root is {self.n ** 1/2}")
    
    @staticmethod
    def hello():
        print("Hello User!")

a = Calculator(enter)
a.hello()
a.square()
a.cube()
a.square_root()
