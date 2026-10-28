# User needs to give the start of mothly income to have a base number for the rest of the program to work with.
income = float(input("Enter your monthly income: $"))

# Income needs to be a positive number.
if income < 0:
    print("Error: Income must be a minimum of $0!")
    exit()

# Input fixed expenses
rent = float(input("Enter monthly rent: $"))
utilities = float(input("Enter monthly utilities: $"))
subscriptions = float(input("Enter monthly subcriptions: $"))
food = float(input("Enter average food expenses: $"))
# Factor in debts and other costs
etc = float(input("Enter total remaining expenses that does not fall in the other categories: $"))

# Consildate number
motnhly_total = rent + utilities + subscriptions + food + etc

# Add limits
rent >= 0.00
utilities >= 0.00
subscriptions >= 0.00
food >= 0.00
etc >= 0.00

# Make the monthly never reach below zero
motnhly_total >= 0.0

# Check for negative expenses
if motnhly_total < 0:
    print("Total: $0.00")    
    exit()

# Final parameters
remaining_budget = income - motnhly_total
if remaining_budget < 0:
    print("Error: Monthly budget cannot be calculated due to the total available fund being depleted.")
else:
    print("\n----- Monthly Budget Below -----")
    print(f"Monthly Income: ${income:.2f}")
    print(f"Fixed Expenses: ${motnhly_total:.2f}")
    print(f"Remaining Budget: ${remaining_budget:.2f}")