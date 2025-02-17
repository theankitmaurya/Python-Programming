# If the names of 2 friends are same; what will happen to the program in problem 6?

d = {}

name = input("Enter your Name: ")
lang = input("Enter your language: ")
d.update({name : lang})

name = input("Enter your Name: ")
lang = input("Enter your language: ")
d.update({name : lang})

name = input("Enter your Name: ")
lang = input("Enter your language: ")
d.update({name : lang})

name = input("Enter your Name: ")
lang = input("Enter your language: ")
d.update({name : lang})

print(d)

# Until coming to the next same name it will have the language as it has before but after entering the same name with different language can update the language and change the previous language
