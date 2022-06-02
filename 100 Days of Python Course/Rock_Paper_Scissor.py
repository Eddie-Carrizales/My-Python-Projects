# Author:      Eddie F. Carrizales
# Date:        06/01/2022
# Description: Rock, Paper, Scissors

import random

computer = random.randint(0,2)

user = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

# note that this could be replaced with a list game = ["Rock", "Paper", Scissors]
# and then we simply grab from the list using the index instead of using all these if else conditionals
if computer == 0:
    print("Computer chose: Rock")
elif computer == 1:
    print("Computer chose: Paper")
else:
    print("Computer chose: Scissors")

if user == 0:
    print("You chose: Rock")
elif user == 1:
    print("You chose: Paper")
elif user == 2:
    print("You chose: Scissors")
else:
    print("You entered invalid input.")


if computer == 0 and user == 2 or computer == 1 and user == 0 or computer == 2 and user == 1:
    print("You loose!")
elif computer == 0 and user == 1 or computer == 1 and user == 2 or computer == 2 and user == 0:
    print("You won!")
elif computer == 0 and user == 0 or computer == 1 and user == 1 or computer == 2 and user == 2:
    print("Its a tie!")
