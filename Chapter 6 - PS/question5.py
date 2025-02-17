# Write a program which finds out whether a given name is present in a list or not.

container = ["Ankit", "Rohan", "Shubham", "Raj", "Devansh"]

name = input("Enter you name: ")

if (name in container):
    print("Your name is in the list")
else:
    print("Your name is not in the list")
