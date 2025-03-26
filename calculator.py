import math
print("Welcome to the calculator!")
result = 0

# Get a valid operation
while True:
    operation = input("Choose an operation: +, -, *, /, ** (exponentiation), %, square root (you can just type root, it will only use first number but "
    "will ask for the secoond number): ")
    if operation in {"+", "-", "*", "/", "**", "%", "square root", "root"}:
        break
    print("Invalid operation! Please choose a valid operator.")

while True:
    # Loop until valid numbers are entered
    while True:
        try:
            first_number = int(input("Choose the first number: "))
            second_number = int(input("Choose the second number: "))
            break  # Exit loop if both inputs are valid
        except ValueError:
            print("Invalid input! Please enter a valid number.")



    # Perform calculation
    if operation == "+":
        result = first_number + second_number
    elif operation == "-":
        result = first_number - second_number
    elif operation == "*":
        result = first_number * second_number
    elif operation == "/":
        if second_number == 0:
            print("Error: Cannot divide by zero.")
            continue  # Go back to asking for numbers
        result = first_number / second_number
    elif operation == "**":
        result = first_number ** second_number
    elif operation == "%":
        result = first_number * second_number / 100
        print(result)
    elif operation == "square root" or operation == "root":
        result = math.sqrt(first_number)
    print(f"Result: {result}")
    break