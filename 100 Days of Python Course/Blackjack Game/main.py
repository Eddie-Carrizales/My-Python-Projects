# Author:      Eddie F. Carrizales
# Date:        06/06/2022
# Description: Blackjack game
import random
import blackjack_art

# ----Blackjack Game Rules-----
# The deck is unlimited in size
# There are no jokers
# The Jack/Queen/king all count as 10
# The Ace can count as 11 or 1
# The cards in this list have equal probability of being drawn
# Cards are not removed from the deck as they are drawn
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Bool to determine when the game has ended
end_of_game = False

def sum_cards(hand_cards):
    """This function will add up all of your cards and give you the total"""
    total = 0
    for card in hand_cards:
        total += card
    return total

def convert_ace(user_cards):
    """This function will convert one ace (with default value of 11) to a value of 1 """
    index = user_cards.index(11)
    user_cards[index] = 1

while not end_of_game:
    # Initialization of lists and bool
    player_cards = []
    computer_cards = []
    isHitting = True

    print(blackjack_art.logo) # prints game logo

    # give two cards to player and dealer(computer)
    player_cards.append(random.choice(cards))
    player_cards.append(random.choice(cards))
    computer_cards.append(random.choice(cards))
    computer_cards.append(random.choice(cards))

    # initial player and computer score based on given cards
    player_score = sum(player_cards)
    computer_score = sum(computer_cards)

    # loops to convert an ace from 11 to a 1 to prevent a score above 21 if a player starts with two 11's
    while player_score > 21 and 11 in player_cards:
        convert_ace(player_cards)
        player_score = sum(player_cards)
    while computer_score > 21 and 11 in computer_cards:
        convert_ace(computer_cards)
        computer_score = sum(computer_cards)

    # if someone knows how the code works they can guess that if the first dealer/computer card is a 1, then
    # the second card must be 11 since the sum will be 22. To solve this we can reverse the list makes and
    # make it impossible to know since we cannot see the dealers/computers second card (this is done only once).
    computer_cards.reverse()

    # loop to tell the player their current cards and the computer's first card, as well as allow the player to
    # keep receiving more cards if they want.
    while player_score <= 21 and isHitting == True:
        print(f"    Your cards are: {player_cards}, current score: {player_score}")
        print(f"    Computer's first card: {computer_cards[0]}")

        get_card = input("Type \'y\' to get another card, type \'n\' to pass: ")

        if get_card == "y":
            player_cards.append(random.choice(cards))
            player_score = sum(player_cards) # updates player score after they receive a card

            # If the players score becomes greater than 21 after receiving a card, and they have Aces
            # this loop will convert those Aces(11) to 1's and update the score
            while player_score > 21 and 11 in player_cards:
                convert_ace(player_cards)
                player_score = sum(player_cards)
        else:
            isHitting =  False # if the user did not want a card, then isHitting becomes False and loop ends

    # After the player has the cards he wants to keep, the computer keep hitting as long as its score is less than 17
    # However, if the score becomes greater than 21 after a hit, and the computer/dealer has Aces, each one of those
    # will be turned from 11 to 1, one by one as required.
    while computer_score < 17:
        computer_cards.append(random.choice(cards))
        computer_score = sum(computer_cards)
        # If the computers score becomes greater than 21 after receiving a card, and they have Aces
        # this loop will convert those Aces(11) to 1's and update the score
        while computer_score > 21 and 11 in computer_cards:
            convert_ace(computer_cards)
            computer_score = sum(computer_cards)

    print(blackjack_art.line)
    print(f"    Your final hand: {player_cards}, final score: {player_score}")
    print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")

    # conditional statements to display if the player won or lost, or if there was a draw with the computer
    if player_score > 21:
        print("    You went over. You lose.")
    elif player_score <= 21 and computer_score <= 21 and player_score < computer_score: # correct
        if computer_score == 21:
            print("    You lost, computer got Blackjack!")
        else:
            print("    You lost, computer score was closer to 21.")
    elif player_score <= 21 and player_score > computer_score:
        if player_score == 21:
            print("    You won, you got Blackjack!")
        else:
            print("    You Won, your score was closer to 21!")
    elif player_score <= 21 and computer_score > 21:
        print("    You won, computer went over!")
    elif player_score == 21 and computer_score == 21:
        print("    Computer has a Blackjack, you lose.")
    else:
        print("    Draw")
    print(blackjack_art.line)

    # Asks the user if they want to play another game of Blackjack, if user enters 'n' game ends
    # otherwise it is implied that the user wants to keep playing
    play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if play_game == "n":
        end_of_game = True