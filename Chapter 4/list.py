# List are mutable, on the other hand strings are immutable.
# Any type of data can be stored in a list.
# We can use slicing in list just like slicing in strings.

friends = ["Apple", "Banana", 5, 23.9, False, "Shubham", "Rohan"]

print(friends[0])
friends[0] = "Mango"

print(friends[0])
print(friends[4])

print(friends[1:4])
