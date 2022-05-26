# Author:      Eddie F. Carrizales
# Date:        05/26/2022
# Description: Tip Calculator

print("Welcome to the tip calculator.")

total_bill = float(input("What is the total bill? $"))
percent_tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

# calculations
bill_tip = percent_tip / 100 * total_bill
bill_with_tip = bill_tip + total_bill

people_split = int(input("How many people to split the bill? "))
bill_of_each_person = round(bill_with_tip / people_split, 2)  # round to two decimals
bill_of_each_person = "{:.2f}".format(bill_of_each_person)  # used to format it so that zeroes also show when showing 2 decimals

print(f"Each person should pay ${bill_of_each_person}")



