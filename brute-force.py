import string
import time
import subprocess
import tkinter as tk
from tkinter import messagebox
print("Welcome to the brute forcer!")
ls = input("Choose 1 for line overwrite, or choose 2 for line spam: ")
if ls == "1":
    while True:
        try:
            speed = float(input("Choose a speed for Brute Forcing (in seconds, e.g., 0.1 for medium): "))  # Allow floating point input
            if speed <= 0:
                print("Speed must be greater than 0. Please try again.")
                continue
            break  # Exit loop if input is valid
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    text = input("Enter String for Brute Force: ")
    temp = ""
    for ch in text:
        for i in string.printable:
            print(f"{temp}{i}", end="\r", flush=True)  # Overwrites the line instead of spamming new lines
            time.sleep(speed)  # Sleep for the floating point speed
            if i == ch:
                temp += ch
                break
    print("\nBrute force complete!")
    try:
        subprocess.run(["python3", "root program.py"])
    except FileNotFoundError:
        print("Root program not found! Check that it exists in the same directory as this file.")
        messagebox.showwarning("File Not Found", f"Error: root program not found!\nMake sure the file exists.")
    except subprocess.CalledProcessError:
        print(f"The program ran into an error and cannot run. Try again.")
        messagebox.showwarning("Execution Error", f"Error: the program encountered an issue and did not run successfully.")
elif ls == "2":
    while True:
        try:
            speed = float(input("Choose a speed for Brute Forcing (in seconds, e.g., 0.1 for medium): "))  # Allow floating point input
            if speed <= 0:
                print("Speed must be greater than 0. Please try again.")
                continue
            break  # Exit loop if input is valid
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    text = input("Enter String for Brute Force: ")
    temp = ' '
    for i in string.printable:
        print(f"{temp}{i}")  # Line spam effect
        time.sleep(speed)  # Sleep for the user-defined speed
        if i == ch:
            temp += ch
            break
    print("\nBrute force complete!")
    try:
        subprocess.run(["python3", "root program.py"])
    except FileNotFoundError:
        print("Root program not found! Check that it exists in the same directory as this file.")
        messagebox.showwarning("File Not Found", f"Error: root program not found!\nMake sure the file exists.")
    except subprocess.CalledProcessError:
        print(f"The program ran into an error and cannot run. Try again.")
        messagebox.showwarning("Execution Error", f"Error: the program encountered an issue and did not run successfully.")
    except TypeError:
        print("typeError")