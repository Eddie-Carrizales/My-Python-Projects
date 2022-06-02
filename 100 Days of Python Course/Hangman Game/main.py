# Author:      Eddie F. Carrizales
# Date:        06/02/2022
# Description: Hangman Game

import random
import hangman_art
import hangman_wordlist

# Intro
print("Welcome to The Hangman Word Guessing Game!")
print(hangman_art.logo)

# Used to choose a random word from our word_list
chosen_word = random.choice(hangman_wordlist.word_list)

# Uncomment code below to see the chosen word.
#  print(f"Psst, the word is \"{chosen_word}.\"")

# Create a display list with all the blanks that is the size of the word randomly selected
display = ["_"] * len(chosen_word)

# list of previous guessed words
previously_guessed = []

# The number of lives available to the player
lives = 6

# Bool to determine when it is the end of the game and stop the while loop
end_of_game = False

while end_of_game is False:
    # Will ask our user to guess a letter and will make the users input lowercase (In case he entered an uppercase letter)
    user_guess = str(input("Guess a letter: ").lower())

    if user_guess in previously_guessed:
        print(f"You have already guessed \"{user_guess}\" before.")
    else:
        previously_guessed.append(user_guess)

        # checks if the letter the user guessed in our word
        for i in range(len(chosen_word)):
            if chosen_word[i] == user_guess:
                display[i] = user_guess

        # if the user_guess is not in the random chosen word, we will decrease one life
        if user_guess not in chosen_word:
            lives -= 1
            print(f"You guessed \"{user_guess}\" but it was not in the word. You lose a life ({lives} left).")
            # If the number of lives is equal to zero then we end the game and the player/user has lost
            if lives == 0:
                end_of_game = True
                print("GAME OVER, YOU LOSE!")
                print(f"The word was {chosen_word}.")
        else:
            print(f"You guessed \"{user_guess}\" and it was in the word.")

    # Prints the hangman stage we are at
    print(hangman_art.stages[lives])

    # Displays what we have guessed correctly in our word
    word_display = ""
    for letter in display:
        word_display += letter + " "
    print(word_display)

    # If there are no more blanks in our display, then we have guessed everything, and we won
    if "_" not in display:
        end_of_game = True
        print("YOU GUESSED THE WORD, YOU WON!\n")