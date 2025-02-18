'''
-1 -> water
0 -> gun
1 -> snake
'''

import random

computer = random.choice([-1, 0, 1])
youStr = input("Enter your choice: ")

youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {-1: "Water", 0: "Gun", 1: "Snake"}

you = youDict[youStr]

print(f"You chose: {reverseDict[you]}\nComputer chose: {reverseDict[computer]}")

if (computer == you):
    print("It's a draw")

else:
    if (computer == -1 and you == 1):
        print("You win!")
    elif(computer == -1 and you == 0):
        print("You lose!")
    elif(computer == 0 and you == 1):
        print("You lose!")
    elif(computer == 0 and you == -1):
        print("You lose!")
    elif(computer == 1 and you == 0):
        print("You win!")
    elif(computer == 1 and you == -1):
        print("You lose!")
        
    else:
        print("Something went wrong!")
