# Author:      Eddie F. Carrizales
# Date:        06/04/2022
# Description: Blind Auction program
import os
from bid_art import logo

print(logo)
print("Welcome to the secret auction program.")
bidding_finished = False  # bool to end the auction when there are no more bidders bidding
bidders = {}  # dictionary to keep a name and bid together
highest_bid = 0

while bidding_finished == False:
    # input statements to request the names and bids from the bidders
    name = str(input("What is your name?: ").lower())
    bid = int(input("What is your bid?: $"))
    other_bidders = str(input("Are there any other bidders? Type \"yes\" or \"no\": ").lower())

    # conditional to keep track of the highest bid
    if bid > highest_bid:
        highest_bid = bid
        # dictionary to tie a bid to a name since bids are technically unique and if two people enter the same bid
        # amount, the first person who made the highest bid will be the winner.
        bidders[highest_bid] = name

    if other_bidders == "yes":
        os.system('clear')  # will clear the console so that the next person can bid and the action stays blind
        # note: print("\n"*100) can be used instead if the console throws clearing error because clearing the console
        # will vary depending on the terminal being used.
    else:
        bidding_finished = True
        print(f"The winner is {bidders[highest_bid].capitalize()} with a bid of {highest_bid}")
