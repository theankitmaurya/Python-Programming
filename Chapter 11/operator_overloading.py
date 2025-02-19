class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num):
        return self.n + num.n

n = Number(1)
m = Number(2)

print(n + m)

# Operators Overloading in Python ->
# Operators in Python can be overloaded using Dunder methods.
# These methods are called when a given operator is used on the objects.

# Operators in Python can be overloaded using the following methods:
# p1 + p2 # p1.__add__(p2)
# p1 - p2 # p1.__sub__(p2)
# p1 * p2 # p1.__mul__(p2)
# p1 / p2 # p1.__truediv__(p2)
# p1 // p2 # p1.__floordiv__(p2)

# Other dunder/magic methods in Python:
# __str__() # used to set what gets displayed upon calling str(obj)
# __len__() # used to set what gets displayed upon calling __len__() or len(obj)
