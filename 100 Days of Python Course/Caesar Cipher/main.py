# Program name: Caesar Cipher
# Author:      Eddie F. Carrizales
# Date:        06/03/2022
# Description: This program encodes and decodes messages using Cesar's Cipher by shifting the letters around.

import art

print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
isRunning = True  # boolean to determine if the program will keep running/repeating or stop.

def caesar_cipher(direction_input, text_input, shift_input):
    final_text = ""
    # This if conditional will change the direction by making the shift negative
    if direction_input == "decode":
        shift_input *= -1
    # This for loop will go through each character in the text_input and shift it accordingly or add it if not in the alphabet
    for char in text_input:
        if char in alphabet:
            letter_pos = alphabet.index(char)
            final_text += alphabet[letter_pos + shift_input]
        else:
            final_text += char
    print(f"Here is the {direction_input}d result {final_text}")

while isRunning:
    # Requesting inputs from the user
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # will reset the shift to start from the beginning of the alphabet, this helps for large numbers that are greater than 26
    shift = shift % 26

    # Call to function
    caesar_cipher(direction, text, shift)

    # Request input to determine if the while loop/program should keep running or stop
    run_again = input("Type \"yes\" if you want to run again. Otherwise type \"no\".\n").lower()
    if run_again == "no":
        isRunning = False
