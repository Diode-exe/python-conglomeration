import subprocess
import tkinter as tk
from tkinter import messagebox
print("Welcome to the infinite counter! This will make your CPU very warm, depending on your cooling solution.")
number = 0
delay = input("Enter the amount of time to wait before calculating the next number, or press Enter to have no delay: ")
# max = input("Enter the number to stop at, or press Enter to give no limit: ")
ls = input("Enter 1 to overwrite previous lines or press 2 to not: ")
if ls == "1":
    while True:
        number = number + 1
        print(number)
#        if number == max:
#            exit
elif ls == "2":
    while True:
        number = number + 1
        print(number, end="\r", flush=True)
        if number == max:
            try:
                subprocess.run("python3", "root program.py", check=True)
            except FileNotFoundError:
                print("Root program not found! Check that it exists in the same directory as this file.")
                messagebox.showwarning("File Not Found", f"Error: root program not found!\nMake sure the file exists.")
            except subprocess.CalledProcessError:
                print(f"The program ran into an error and cannot run. Try again.")
                messagebox.showwarning("Execution Error", f"Error: the program encountered an issue and did not run successfully.")