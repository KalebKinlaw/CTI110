# Kaleb Kinlaw
# CTI - 110
# PT5T1 - Functions
# 10/24/23

def main():
  print("Hello world!")
  burger = 4.99000001
  print_money(burger)
  print_money(12)
  print_money(0.3)
def print_money(amount): 
  print("$",format(amount, ".02f"))
# Now, start the program
main()