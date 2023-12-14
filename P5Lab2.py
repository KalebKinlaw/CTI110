"""
Kaleb Kinlaw
CTI - 110
P5Lab2 - More Functions 
11/2/23
"""

# First, print a table of squares
def main():
  print("P5Lab2 - Squares ")
  print("number\tnumber squared")
  for num in range(1, 11):
    num_squared = square(num)
    print_row(num, num_squared)




def square(number):
  """input: a number
  output: the number squared."""
  square = number * number
  return square

def print_row(num, num_squared):
  print(num, '\t\t', num_squared)


main()