import os
import functions
from classes_9 import Budget

os.system('cls' if os.name == 'nt' else 'clear')
_name = input('Enter your name: ')
print(f"Hey {_name}, this is BudgetBuddy! Your personal Budgeting Assistant.")

while True:
    try:
        income = float(input("Enter monthly income (numbers only): "))
        break
    except:
        print("numbers only")

total_expenses = []

grocery = Budget("Grocery")
car = Budget("Car")

print("Grocery expenses:")
grocery.add_expenses()
print("Car expenses:")
car.add_expenses()

exp_grocery = grocery.get_expenses()
total_expenses.append(exp_grocery)

bal = functions.calc_balance(income, sum(total_expenses))

functions.financial_status(bal)

grocery.get_expenses_list()



