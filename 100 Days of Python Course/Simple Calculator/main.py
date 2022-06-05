# Author:      Eddie F. Carrizales
# Date:        06/05/2022
# Description: Simple calculator that can add, subtract, multiply, and divide numbers.

# Calculator
from calculator_art import logo

# Add
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

# Dictionary of the operations
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))
    keep_calculating = True

    while keep_calculating == True:
        for symbol in operations:
            print(symbol)

        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))

        calculation_function = operations[operation_symbol]
        result = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {result}")

        continue_calc = input(f"Type \'y\' to continue calculating with {result}, or type \'n\' to start a new calculation: ")

        if continue_calc == "y":
            num1 = result
        else:
            keep_calculating = False
            calculator()


calculator()