import math
from fractions import Fraction
import time
import subprocess
import tkinter as tk
from tkinter import messagebox
print("Welcome to the calculator!")
result = 0
fractionschoice = input("Choose 1 for standard operation math and 2 for fraction math: ")
if fractionschoice == "1":
    print ("Welcome to operation math. Follow the on screen instructions. Advancing in 3 seconds.")
    time.sleep(3)
    # Get a valid operation
    while True:
        operation = input("Choose an operation: +, -, *, /, ** (exponentiation), %, square root (you can just type root, it will only use first number but "
        "will ask for the secoond number), : ")
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
if fractionschoice == "2":
    while True:
        try:
            ND1 = int(input("Numerator and denominator: "))
        except ValueError:
            print("Invalid input. Choose a number, please.")

        try:
            ND2 = int(input("Numerator and denominator: "))
        except ValueError:
            print("Invalid input. Choose a number, please.")
        

        try:
            operation = input("+ or -")
        except operation not in {"+", "-"}:
            print("Choose + or -")

        while True:
            if operation == "+":
                result = ND1 + ND2
                break
            elif operation == "-":
                result = ND1 - ND2
                break

        print(result)
 #       try:
 #           subprocess.run("python", "root program.py")
 #       except FileNotFoundError:
  #          print("Root program not found! Check that it exists in the same directory as this file.")
   #         messagebox.showwarning("File Not Found", f"Error: root program not found!\nMake sure the file exists.")
    #    except subprocess.CalledProcessError:
     #       print(f"The program ran into an error and cannot run. Try again.")
      #      messagebox.showwarning("Execution Error", f"Error: the program encountered an issue and did not run successfully.")
else:
    print("Invalid selection! Exiting...")