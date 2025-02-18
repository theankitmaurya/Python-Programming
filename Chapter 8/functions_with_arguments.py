name = input("Enter your name: ")
greetings = "Thank you"

def goodDay(name, greetings):
    print("Good Day, " + name)
    print(greetings)

goodDay(name, greetings) # Here, the function is taking an argument

name = input("Enter your name: ")
greetings = "Thank you"

def goodDay(name, greetings):
    print("Good Day, " + name)
    print(greetings)
    return "done" # Here, we used return so that in 'a' a value will go in return of the function. This value can be anything either it is a number or a string

a = goodDay(name, greetings)
print(a)

# Function can take more than one argument
