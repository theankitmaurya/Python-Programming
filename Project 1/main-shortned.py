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
    if ((computer - you) == -1 or (computer - you) == 2):
        print("You lose!")
    else:
        print("You win!")
