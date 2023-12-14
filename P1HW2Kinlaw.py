"""
CTI-110 P1HW2 - Travel Expense
Kaleb Kinlaw
9/15/23

This program calculates and displays travel expenses. 
"""

print("Enter your budget?")
budget = input()
print("What is the travel destination?")
travel_destination = input()
print("How much will you spend on gas?")
gas = input()
print("How much will you spend on accomodations?")
accomodations = input()
print("How much will you spend on food?")
food = input()

# Add expenses 
gas = "250"
accomodations = "600"
food = "300"
sum = (250 + 600 + 300)
print("The sum is ", sum)
# Subtract from budget 
budget = 1200 
remaining_balance = (1200 - sum)
print("The remaining balance is", remaining_balance)