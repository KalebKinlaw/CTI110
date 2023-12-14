"""
CTI 110
P1HW1 - Variables
kinlawk
9/5/23

Do some basic output with numbers
1. ask for an int
2. square it and then cube it
3. ask for another int
4. add them and multiply them

"""
# PART ONE: NUMBERS
# variables, first and second
first = 0
second = 0

print("Enter integer:")
first = int(input()) # take input. then convert it to int
print(first, "squared is", first * first)
print("and", first, "cubed is", first * first * first, "!!")

# get another int
print("Enter another integer:")
second = int(input())
# TODO: print the number, not the words first and second
print(first, "+", second, "=", first + second)
print(first, "*", second, "=", first * second)




# PART TWO: MOVIES
# Three variables
# int - year of the movie
# float - the gross (in million dollars)
# string - movie name
# finally, print a quote from the movie

year = 2023
gross = 853.24 # mil $

# Print out this information 
# Then print a movie quote
print("""

"Oppenheimer released in 2023 and grossed $853.24."

""")


print("""

 "Now I am become Death, the destroyer of worlds."

""")
