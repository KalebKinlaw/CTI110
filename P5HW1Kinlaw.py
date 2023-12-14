# Kaleb Kinlaw
# CTI - 110
# P5HW1 - Math Quiz
# 11/15/23

import random
number = random.randint(1, 250)
print("Welcome to Math Quiz")
print("MAIN MENU:")
print("---------------------")
print("1. Adding random numbers")
print("2. Subtracting random numbers")
print("3. Exit")
choice = int(input("Enter your choice: "))
if choice == 1:
    answer = None
    while answer != number + number:
        print("What is", number, "+", number, "?")
        answer = int(input("Enter your answer: "))
        if answer == number + number:
            print("Correct!")
        else:
            print("Incorrect! Your answer is too high or too low. Please try again.")
elif choice == 2:
    answer = None
    while answer != number - number:
        print("What is", number, "-", number, "?")
        answer = int(input("Enter your answer: "))
        if answer == number - number:
            print("Correct!")
        else:
            print("Incorrect! Your answer is too high or too low. Please try again.")
answer = "yes"
while answer == "yes":
    # code here
    answer = input("Would you like to continue? (yes/no) ")