import math

# Print the initial menu to advise users
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")
print("Enter either 'investment' or 'bond' from the menu above to proceed")

# Get user input and convert to lowercase
choice = input().lower()

# Check user input and run the right calculator
if choice == "investment":
    # Get user input for investment calculator
    principal = float(input("Enter the amount of money you are depositing: "))
    rate = float(input("Enter the interest rate (as a percentage): ")) / 100
    years = int(input("Enter the number of years you plan on investing: "))
    interest = input("Do you want simple or compound interest? ").lower()

    # Calculate total amount
    if interest == "simple":
        total = principal * (1 + rate * years)
    elif interest == "compound":
        total = principal * math.pow((1 + rate), years)
    else:
        print("Error: Invalid input for interest type")
        exit()

    # Print out answer
    print("Total amount after {} years: {:.2f}".format(years, total))

elif choice == "bond":
    # Get user input for bond calculator
    present_value = float(input("Enter the present value of the house: "))
    rate = float(input("Enter the interest rate: "))
    months = int(input("Enter the number of months to repay the bond: "))

    # Calculate monthly repayment amount
    i = (rate / 100) / 12
    repayment = (i * present_value) / (1 - math.pow(1 + i, -months))

    # Print out answer
    print("Monthly repayment: {:.2f}".format(repayment))

else:
    print("Error: Invalid input for calculator type")
