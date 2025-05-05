import math
from fractions import Fraction
import time
import subprocess
import tkinter as tk
from tkinter import simpledialog, messagebox

print("Welcome to the calculator!")
result = 0
fractionschoice = simpledialog.askstring("Operation","Choose 1 for standard operation math and 2 for fraction math: ")

if fractionschoice == "1":
    print("Welcome to operation math. Follow the on-screen instructions.")
    time.sleep(3)

    while True:
        operation = input("Choose an operation: +, -, *, /, ** (exponentiation), %, root: ")
        if operation in {"+", "-", "*", "/", "**", "%", "root"}:
            break
        print("Invalid operation! Please choose a valid operator.")

    while True:
        try:
            first_number = int(input("Choose the first number: "))
            second_number = int(input("Choose the second number: "))
            break  
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    if operation == "+":
        result = first_number + second_number
    elif operation == "-":
        result = first_number - second_number
    elif operation == "*":
        result = first_number * second_number
    elif operation == "/":
        if second_number == 0:
            print("Error: Cannot divide by zero.")
        else:
            result = first_number / second_number
    elif operation == "**":
        result = first_number ** second_number
    elif operation == "%":
        result = first_number * second_number / 100
    elif operation == "root":
        result = math.sqrt(first_number)

    print(f"Result: {result}")

elif fractionschoice == "2":
    while True:
        try:
            num1 = int(input("Enter numerator for first fraction: "))
            denom1 = int(input("Enter denominator for first fraction: "))
            num2 = int(input("Enter numerator for second fraction: "))
            denom2 = int(input("Enter denominator for second fraction: "))

            fraction1 = Fraction(num1, denom1)
            fraction2 = Fraction(num2, denom2)

            operation = input("Choose + or -: ")
            if operation not in {"+", "-"}:
                print("Invalid operation! Please choose + or -.")
                continue

            if operation == "+":
                result = fraction1 + fraction2
            else:
                result = fraction1 - fraction2

            print(f"Result: {result}")
            break  

        except ValueError:
            print("Invalid input. Please enter integers for numerators and denominators.")
        except ZeroDivisionError:
            print("Error: Denominator cannot be zero.")

    try:
        subprocess.run(["python3", "root program.py"], check=True)
    except FileNotFoundError:
        print("Root program not found! Check that it exists in the same directory as this file.")
        messagebox.showwarning("File Not Found", "Error: root program not found!\nMake sure the file exists.")
    except subprocess.CalledProcessError:
        print("The program ran into an error and cannot run. Try again.")
        messagebox.showwarning("Execution Error", "Error: the program encountered an issue and did not run successfully.")

else:
    print("Invalid selection! Exiting...")
