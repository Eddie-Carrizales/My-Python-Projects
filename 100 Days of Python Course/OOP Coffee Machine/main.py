# Author:      Eddie F. Carrizales
# Date:        06/09/2022
# Description: OOP Coffee Machine- I previously built a Coffee Machine using procedural programming
# This project is a remake of that project using object-oriented programming using resources/documentation
# from The App Brewery educational institution.

# NOTE: Files that have The App Brewery as authors are not mine and do not contain any of my code.

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#object = Class()
coffee_machine = CoffeeMaker()
cashier_machine = MoneyMachine()
coffee_menu = Menu()

is_off = False

while not is_off:
    user_choice = input(f"What would you like? ({coffee_menu.get_items()}): ")

    if user_choice == "report":
        coffee_machine.report()
        cashier_machine.report()
    elif user_choice == "off":
        is_off = True
    else:
        # Finds the drink the user chose from the coffee menu, and returns a user_drink object with that
        # drink's ingredients, name, and cost
        user_drink = coffee_menu.find_drink(user_choice)

        # using the user_drink object with the ingredients attribute we check if we have enough resources to
        # fulfill the order
        if coffee_machine.is_resource_sufficient(user_drink):
            # If we have enough resources, we then make a payment and pass the cost of the users drink
            if cashier_machine.make_payment(user_drink.cost):
                # if the payment is successful, then we make the coffee
                coffee_machine.make_coffee(user_drink)