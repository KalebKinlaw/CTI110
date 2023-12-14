"""
Kaleb Kinlaw
CTI - 110
P4T3 - Three Loops
10/10/23
"""


#Write three loops
# 1. for loop
# 2. while loop 
# 3. while with sentinel 
# for each of theses, do the following 
# Aak the user how many cars they sawy today
# find the total and the average 
MAX_DAYS = 5
day = 1
cars_today = 0
cars_total = 0 


# 1 - for loop
for day in range(1,MAX_DAYS+1):
  print("Day #", day, end=":")
  cars_today = int(input())
  cars_total = cars_total + cars_today
print("Total cars = ", cars_total)
average = cars_total / MAX_DAYS
print("Average per day = ", average)


# 2 - while loop
day = 1
cars_today = 0
cars_total = 0
print("Enter how many cars you saw today: ")
while day < MAX_DAYS:
  print("Day #", day, end=":")
  cars_today = int(input())
  cars_total = cars_total + cars_today
  day = day + 1
print("Total # of cars seen: ", cars_total)
average = cars_total / MAX_DAYS
print("Average per day =", average)


# 3 - while with sentinel
DONE_VALUE = -1
keep_going = True
while keep_going:
  print("Cars seen today: ", end="")
  cars_today = int(input())
  if cars_today == DONE_VALUE:
    keep_going = False
  else:
    cars_total = cars_total + cars_today
print("total cars = ", cars_total)
average = cars_total / day 
print("Average per day = ", average)