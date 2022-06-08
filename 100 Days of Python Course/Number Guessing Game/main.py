# Author:      Eddie F. Carrizales
# Date:        06/07/2022
# Description: Number Guessing Game

import random
import game_art

print(game_art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
random_number = random.randint(1,100)

difficulty = str(input("Choose a difficulty. Type \'easy\' or \'hard\': "))
attempts_remaining = 0

# Give remaining attempts based on difficulty chosen by user
if difficulty == "easy":
    attempts_remaining = 10
elif difficulty == "hard":
    attempts_remaining = 5

print(f"You have {attempts_remaining} attempts remaining to guess the number.")
number_guessed = int(input("Make a guess: "))

# loop to keep asking for attempts, check if the number guessed if greater or lower than the random number
# and reduce attempts remaining each round the user does not guess the number
while attempts_remaining != 0 or number_guessed != random_number:

    if number_guessed > random_number:
        attempts_remaining -= 1
        print("Too high. \nGuess again.")
        print(f"You have {attempts_remaining} attempts remaining to guess the number.")
        number_guessed = int(input("Make a guess: "))
    elif number_guessed < random_number:
        attempts_remaining -= 1
        print("Too low. \nGuess again.")
        print(f"You have {attempts_remaining} attempts remaining to guess the number.")
        number_guessed = int(input("Make a guess: "))
    else:
        print("You guessed it! Yay!")
        attempts_remaining = 0


