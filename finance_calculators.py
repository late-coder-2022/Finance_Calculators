"""
This program calculates investment return and home loan repayment for users.

The math library will be imported for the power method.

Users' input for menu option supports mix of upper and lower case
letters.

If user chose 'investment':
    ask for deposit amount
    ask for interest rate
    ask for duration of investment
    ask for interest choice either simple or compound
    do the calculation.

If user chose 'bond':
    ask for the present value of the house
    ask for the interest rate
    ask for the repayment months
    do the calculation.
"""

# Import math library for the power of method.
import math

# Display a user menu and ask user to pick either investment or bond option.
print("investment\t - to calculate the amount of interest you'll earn on your investment")
print("bond\t\t - to calculate the amount you'll have to pay on a home loan")
menu_opt = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

if menu_opt == 'investment':
    deposit_amount = float(input("Please input the amount you want to deposit: \n"))
    interest_rate = float(input("Please enter the interest rate you prefer: \n"))
    invest_year = int(input("Please enter the year you want to invest: \n"))
    interest_mode = input("Please choose either 'simple' or 'compound' interest: \n").lower()
    if interest_mode == 'simple':
        total_amount = round(deposit_amount*(1+((interest_rate/100)*invest_year)), 2)
        print(f"The total amount including the simple interest will be R{total_amount}\n")
    elif interest_mode == 'compound':
        total_amount = round(deposit_amount*math.pow((1+(interest_rate/100)), invest_year), 2)
        print(f"The total amount including the compound interest will be R{total_amount}\n")
elif menu_opt == 'bond':
    present_value = float(input("Please input the present value of the house: \n"))
    interest_rate = float(input("Please enter the interest rate you prefer: \n"))
    repay_month = int(input("Please enter the number of months you plan to repay the bond: \n"))
    monthly_repay = round((((interest_rate/100)/12)*present_value)/(1-(1+((interest_rate/100)/12))**(-repay_month)), 2)
    print(f"Your monthly repayment will be R{monthly_repay}.\n")
else:
    print("Please choose either 'investment' or 'bond' from the menu.\n")
