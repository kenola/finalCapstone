import operator

OPERATIONS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}

def calculate(num1, num2, op):
    return OPERATIONS[op](num1, num2)

def write_to_file(num1, num2, op, result):
    with open("equations.txt", "a") as f: # Open file in append mode
        f.write(f"{num1} {op} {num2} = {result}\n") # Write equation to file


def read_from_file(file_name):
    try:
        with open(file_name, "r") as f: # Open file in read mode
            equations = f.readlines()# Read all lines in file as a list
        for eq in equations:
            equation_parts = eq.strip().split()  # Split equation into parts (num1, op, num2)
            if len(equation_parts) == 3: # Check if equation is properly formatted
                num1, op, num2 = equation_parts # Assign equation parts to variables
                try:
                    num1 = float(num1)
                    num2 = float(num2)
                    if op not in OPERATIONS.keys():  # Check if operator is valid
                        raise ValueError("Invalid operator.")
                    result = calculate(num1, num2, op) # Calculate result
                    print(f"{num1} {op} {num2} = {result}") # Print equation and result
                except ValueError as e: # Handle invalid input error
                    print(f"Error: {e}")
            else:
                print(f"Invalid equation: {eq}")
    except FileNotFoundError: # Handle file not found error
        print("File not found.")
        get_file_name()  # Prompt user to enter file name again


def get_file_name():
    file_name = input("Enter the name of the file: ")# Prompt user for file name
    read_from_file(file_name)# Read equations from file

def get_input():
    while True:
        try:
            num1 = float(input("Enter the first number: "))# Prompt user for first number
            num2 = float(input("Enter the second number: "))# Prompt user for second number
            op = input("Enter the operator (+,-,*,/): ")# Prompt user for operator
            if op not in OPERATIONS.keys():# Check if operator is valid
                raise ValueError("Invalid operator.")
            if op == '/' and num2 == 0: # Check for division by zero
                raise ZeroDivisionError("Cannot divide by zero.")
            result = calculate(num1, num2, op)# Calculate result
            print(f"{num1} {op} {num2} = {result}")# Print equation and result
            write_to_file(num1, num2, op, result)# Write equation to file
            break
            break
        except ValueError as e: # Handle invalid input error
            print(f"Error: {e}")
        except ZeroDivisionError as e:# Handle division by zero error
            print(f"Error: {e}")

def main():
    option = input("Enter 1 to calculate or 2 to read from file: ") # Prompt user for option
    if option == '1':
        get_input()# Perform calculation
    elif option == '2':
        get_file_name()# Read equations from file
    else:
        print("Invalid option.")

if __name__ == '__main__':
    main()
