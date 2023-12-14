"""
CTI - 110
P3T2 - Making Choices Part 2 
Kaleb Kinlaw 
9/26/23
"""
# The most simple program, with main()
def main():
  #my_function()
  print("-"*10, "Main Menu", "-"*10)
  print("1. Order Breakfast")
  print("2. Order Lunch")
  print("3. Order Dinner")

  # Let the user choose
  print("Your choice? ", end= "")
  choice = int(input())
  print("You chose:", choice)
  
  # branch (if) on choice 
  if choice == 1: 
    option_1()
  elif choice == 2: 
    option_2()
  elif choice == 3:
    option_3()
  else: 
    print("Sorry, that's not an option.")
def option_1(): 
  print("Ordering Breakfast")
  print("Would you like eggs or pancakes?")
  food = input()
  if food == "eggs":
    print("eggs coming right up!")
  elif food == "pancakes":
    print("with syrup")
  else:
    print("Sorry, we don't have that")
def option_2(): 
  print("Ordering Lunch")
  print("Would you like pizza or a sub?")
  food = input()
  if food == "pizza":
    print("two pepperoni slices coming right up!")
  elif food == "sub":
    print("One sub coming right up!")
  else:
    print("Sorry, we don't have that.")

def option_3():
  print("Ordering Dinner")
  print("Would you like spaghetti or chicken?")
  food == input()
  if food == "spaghetti":
    print("spaghetti coming right up!")
  elif food == "chicken":
    print("chicken coming right up!")
  else: 
    print("sorry, we don't have that.")
# start the program 
main()