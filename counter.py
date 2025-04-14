import subprocess
import time
import tkinter as tk
from tkinter import messagebox

print("Welcome to the infinite counter! This will make your CPU very warm, depending on your cooling solution.")

number = 0

# Handling delay input
delay_input = input("Enter the amount of time to wait before calculating the next number, or press Enter to have no delay: ")
delay = float(delay_input) if delay_input.strip() else 0  # Convert to float if provided, else default to 0

# Handling max number input
max_input = input("Enter the number to stop at, or press Enter to give no limit: ")
max_value = int(max_input) if max_input.strip() else None  # Convert to int if provided, else None (no limit)

# Handling line overwrite preference
ls = input("Enter 1 to overwrite previous lines or press 2 to not: ")

if ls == "1":
    while max_value is None or number <= max_value:
        number += 1
        print(number)
        if delay:
            time.sleep(delay)
    
    # Run root program **after** loop completes
    try:
        subprocess.run(["python3", "root_program.py"], check=True)
    except FileNotFoundError:
        print("Root program not found! Check that it exists in the same directory as this file.")
        messagebox.showwarning("File Not Found", "Error: root program not found!\nMake sure the file exists.")
    except subprocess.CalledProcessError:
        print("The program ran into an error and cannot run. Try again.")
        messagebox.showwarning("Execution Error", "Error: the program encountered an issue and did not run successfully.")

elif ls == "2":
    while max_value is None or number <= max_value:
        number += 1
        print(number, end="\r", flush=True)
        if delay:
            time.sleep(delay)

    # Run root program after reaching max_value
    try:
        subprocess.run(["python3", "root_program.py"], check=True)
    except FileNotFoundError:
        print("Root program not found! Check that it exists in the same directory as this file.")
        messagebox.showwarning("File Not Found", "Error: root program not found!\nMake sure the file exists.")
    except subprocess.CalledProcessError:
        print("The program ran into an error and cannot run. Try again.")
        messagebox.showwarning("Execution Error", "Error: the program encountered an issue and did not run successfully.")
