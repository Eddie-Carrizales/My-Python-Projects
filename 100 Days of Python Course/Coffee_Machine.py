# Author:      Eddie F. Carrizales
# Date:        06/09/2022
# Description: Coin Operated Coffee Machine (has 3 hot flavours)
"""
Has 3 hot flavours
-Espresso - requires 50ml water, 18g coffee - price 1.50
-Latte - 200ml water, 24g coffee, 150ml milk - price 2.50
-Cappuccino - 250ml water, 24g coffee, 100ml milk - price 3.00

Coffee machine starting resources
- 300ml water
- 200ml milk
- 100g coffee
- Money ($0)

Coin operated (US currency)
Penny - 1 cent
Nickel - 5 cents
Dime - 10 cents
Quarter - 25 cents

"""
# Menu of the coffee flavours, the resources required for each, and their cost
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

def check_resources(choice, resources):
    """This function will check to make sure there are enough resources in our coffee machine to keep making coffee"""
    enough_resources = True # boolean to determine when we do not have enough resources

    # Conditionals to determine whether the ingredient is in a flavour and if we have enough of that ingredient to serve
    # the flavour requested. NOTE: This function is reusable for future flavours that may use any combination of
    # these three ingredients.
    if "water" in MENU[choice]["ingredients"]:
        # If there is not enough water in our resources to fulfill our flavor, set not enough_resources to False
        if resources["water"] < MENU[choice]["ingredients"]["water"]:
            enough_resources = False
            print(f"Sorry there is not enough water.") # feedback to the user
    if "milk" in MENU[choice]["ingredients"]:
        if resources["milk"] < MENU[choice]["ingredients"]["milk"]:
            enough_resources = False
            print(f"Sorry there is not enough milk.")
    if "coffee" in MENU[choice]["ingredients"]:
        if resources["coffee"] < MENU[choice]["ingredients"]["coffee"]:
            enough_resources = False
            print(f"Sorry, there is not enough coffee.")

    # If we are missing any resource enough_resources will return False
    return enough_resources

def complete_transaction(choice, resources, money, profit):
    """This function will be called to reduce the resources we will use and the money that it will cost to make our coffee"""

    # If the water ingredient is in our flavour, then reduce the amount of water the ingredient will cost
    if "water" in MENU[choice]["ingredients"]:
        resources["water"] -= MENU[choice]["ingredients"]["water"]
    if "milk" in MENU[choice]["ingredients"]:
        resources["milk"] -= MENU[choice]["ingredients"]["milk"]
    if "coffee" in MENU[choice]["ingredients"]:
        resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]

    # Used to calculate the change we will give back to the user
    change = money - MENU[choice]["cost"]

    # Format the change to two decimal points
    formatted_change = '{0:.2f}'.format(change)

    # Feedback to user
    print(f"Here is ${formatted_change} in change.")
    print(f"Here is your {choice}. Enjoy!")

def process_coins():
    """This function will request coins from the user in integers and convert two their actual values as well as add them up
    this function will return the total inserted."""
    print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * .25
    dimes = int(input("How many dimes?: ")) * .10
    nickles = int(input("How many nickles?: ")) * .05
    pennies = int(input("How many pennies?: ")) * .01

    # Calculates total inserted and returns it
    total = quarters + dimes + nickles + pennies
    return total

def machine_report(resources, profit):
    """This function prints the current resources in the machine (water, milk, coffee, and money)"""
    print("Water: " + str(resources["water"]) + "ml")
    print("Milk: " + str(resources["milk"]) + "ml")
    print("Coffee: " + str(resources["coffee"]) + "g")

    # formats the profit to two decimals
    formatted_profit = '{0:.2f}'.format(profit)
    print(f"profits: ${formatted_profit}")

def coffee_machine():
    """Function to run our coffee machine"""

    # Starting resources for our coffee machine
    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }
    # Bool to determine when to stop looping and asking the user to coffee flavours
    is_off = False

    # The profit generated in the lifetime of the machine
    profit = 0

    # loop that keeps running while our coffee machine is not off, will stop when our machine is off.
    while not is_off:
        coffee_choice = input("What would you like? (espresso/latte/cappuccino): ")

        # conditional to check what the user entered to determine if the machine should give a report of resources,
        # turn off, or make a specific coffee flavour ("report" and "off" are supposed to be secret keywords)
        if coffee_choice == "report":
            machine_report(resources, profit) # call to function machine_report() to display current resources
        elif coffee_choice == "off":
            is_off = True
        else:
            has_resources = check_resources(coffee_choice, resources) # call to function check_resources()
            # If the machine has enough resources it will ask the user to enter money
            if has_resources:
                money = process_coins() # Call to function process_coins()

                # If the user entered enough money to cover the cost of the coffee flavour, then complete the transaction
                # otherwise state it is not enough and "refund the money"
                if money >= MENU[coffee_choice]["cost"]:
                    complete_transaction(coffee_choice, resources, money, profit)
                    # Adds the cost of the coffee to the total profits of the machine
                    profit += MENU[coffee_choice]["cost"]
                else:
                    print("Sorry that's not enough money. Money refunded.")

coffee_machine()

