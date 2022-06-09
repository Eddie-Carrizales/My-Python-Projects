# Author:      Eddie F. Carrizales
# Date:        06/08/2022
# Description: This program is a higher or lower game based on instagram celebrities and their followers
# the game consists of guessing which celebrity has more followers on instagram. The more guesses you make
# correctly, the higher score you get.
import random
import game_art
import game_data

def celebrity_info(celebrity):
    """Will grab all the values/data of a particular celebrity and put it into a list"""
    celeb_info = []
    for key in celebrity:
        celeb_info.append(celebrity[key])
    return celeb_info

def generate_celebrities():
    """Will choose two random celebrities from the game_data and make sure they are not the same"""
    celebrity_a = random.choice(game_data.data)
    celebrity_b = random.choice(game_data.data)
    # If the celebrities are the same, select a new random celebrity for b
    while celebrity_a == celebrity_b:
        celebrity_b = random.choice(game_data.data)
    return celebrity_a,celebrity_b

def higher_lower_game():
    """Function to play the higher lower game"""
    print(game_art.logo)
    end_of_game = False # Boolean to determine when to end the game
    score = 0 # Score initialization

    # Call to function to generate the two initial celebrities
    celebrity_a, celebrity_b = generate_celebrities()

    # Loop to keep the game running as long as the player keeps answering correctly
    while not end_of_game:
        # Call to celebrity info function
        celeb_info_a = celebrity_info(celebrity_a)
        celeb_info_b = celebrity_info(celebrity_b)
        # Print statements to display celebrity information
        print(f"Compare A: {celeb_info_a[0]}, a {celeb_info_a[2]}, from {celeb_info_a[3]}.")
        print(game_art.vs)
        print(f"Against B: {celeb_info_b[0]}, a {celeb_info_b[2]}, from {celeb_info_b[3]}.")
        # Print statement to request guess/answer from user
        guess = str(input("Who has more followers? Type \'A\' or \'B\': ").lower())
        print(game_art.separator)
        # Conditional to determine if the user answer will be correct or incorrect
        if celeb_info_a[1] > celeb_info_b[1]:
            answer = "a"
        else:
            answer = "b"
        # If the user answer is correct, their score will go up and celebrity in position b will shift to position a and
        # a new random celebrity will be selected for position b.
        if guess == answer:
            score += 1
            celebrity_a = celebrity_b
            celebrity_b = random.choice(game_data.data)
            while celebrity_a == celebrity_b:
                celebrity_b = random.choice(game_data.data)

            print(f"You're right! Current score: {score}")
            print(game_art.separator)
        else:
            # If the user does not guess correctly, the game ends and the users final score is displayed
            end_of_game = True
            print(f"Sorry, that's wrong. Final score: {score}")
            print(game_art.separator)

higher_lower_game()