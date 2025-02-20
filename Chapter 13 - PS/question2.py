# Write a program to input name, marks and phone number of a student and format it using the format function like below:
# "The name of the student is Ankit, his marks are 88 and phone number is 99999888"

name = input("Enter your name: ")
marks = int(input("Enter your marks: "))
phoneNumber = int(input("Enter your Phone Number: "))

s = "The name of the student is {}, his marks are {} and his phone number is {}".format(name, marks, phoneNumber)

print(s)
