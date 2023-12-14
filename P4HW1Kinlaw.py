"""
Kaleb Kinlaw
CTI - 110
P4HW1 - Score List 
10/27/23
"""

def main_menu():
    print("Welcome to the Score List Program!")
    print("Please select an option from the menu below:")
    print("1. Add a score to a list")
    print("2. Quit")
    choice = input()
    if choice == '1':
      print("Enter the scores:")
      score_list = []
      for i in range(0, 100):
        score = input()
        score_list.append(int(score))
      print("The scores are:")
      for score in score_list:
        if score < 0 or score > 100: 
          print("Invalid. Scores must be between 0 to 100.")
      if choice == '2':
        print("Ok. Goodbye.")

# print the lowest score
def lowest_score(score_list):
  lowest_score = min(score_list)
  print("The lowest score is:", lowest_score)
  
# print the highest score
def highest_score(score_list):
  highest_score = max(score_list)
  print("The highest score is:", highest_score)
  
# print the average score
def average_score(score_list):
  total = 0
  for score in score_list:
    total += score
  average = total / len(score_list)
  print("The average score is:", average)