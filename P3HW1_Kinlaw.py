"""
Kaleb Kinlaw
CTI - 110
P3HW1 
10/4/2023

# This program takes a number grade , determines average and displays letter grade for average.

"""

# Enter grades for six modules

mod_1 = input('Enter grade for Module 1: ')
mod_2 = input('Enter grade for Module 2: ')
mod_3 = input('Enter grade for Module 3: ')
mod_4 = input('Enter grade for Module 4: ')
mod_5 = input('Enter grade for Module 5: ')
mod_6 = input('Enter grade for Module 6: ')

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
# TO DO: determine lowest, highest , sum and average for grades

low = min(grades)
high = max(grades)
my_sum = sum(grades)
my_average = my_sum / len(grades)


# determine letter grade for average

if my_average == 90:
  print("Your grade is: A")
else: 
  print("Better luck next time")
if my_average == 80:
  print("Your grade is: B")
else:
  print("Better luck next time")
if my_average == 70:
  print("Your grade is: C")
else:
  print("Better luck next time")
if my_average == 60: 
  print("Your grade is: D")
else:
  print("Your grade is: F. Better luck next time")