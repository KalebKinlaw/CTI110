"""
Kaleb Kinlaw
CTI - 110
P4HW2 
10/27/23
"""

def main():
    print("Choose an option from below:")
    print("1. Calculate")
    print("2. Quit")
    choice = input("Enter your choice: ")
    if choice == "1":
        print("Enter the employee's name:")
        name = input()
        print("How many hours did", name, "work?")
        hours_worked = float(input())
        print("What is", name, "'s pay rate?")
        pay_rate = float(input())
        print("Hours Worked", "Pay Rate", "Overtime", "Overtime Pay", "RegHour Pay", "Gross Pay")
        print("------------------------------------------------------------------------------")
        overtime = hours_worked - 40
        overtime_pay = overtime * pay_rate * 1.5
        reg_hour_pay = hours_worked * pay_rate
        gross_pay = reg_hour_pay + overtime_pay
        print(hours_worked, pay_rate, overtime, overtime_pay, reg_hour_pay, gross_pay)
        gross_pay = reg_hour_pay + overtime_pay 
        print(hours_worked, pay_rate, overtime, overtime_pay, reg_hour_pay, gross_pay)
      
    elif choice == "2":
        print("Goodbye!")