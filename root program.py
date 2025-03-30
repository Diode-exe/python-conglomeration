import subprocess
import tkinter as tk
from tkinter import messagebox

# Initialize Tkinter once to avoid window flashing
root = tk.Tk()
root.withdraw()

programs = {
    "1": "brute force.py",
    "2": "brute force ls.py",
    "3": "random number.py",
    "4": "calculator.py",
    "5": "counter.py",
}

while True:
    choice = input("Choose 1 for brute forcer (not real hacking tool), press 2 for brute forcer (line spam), "
                   "press 3 for number guessing game, press 4 to start the calculator, press 5 to start the infinite counter "
                   "press x to test or type bye or exit to exit: ")

    if choice in programs:
        try:
            subprocess.run(["python3", programs[choice]], check=True)
        except FileNotFoundError:
            print(f"{programs[choice]} not found! Check that it exists in the same directory as this file.")
            messagebox.showwarning("File Not Found", f"Error: {programs[choice]} not found!\nMake sure the file exists.")
        except subprocess.CalledProcessError:
            print(f"The program {programs[choice]} ran into an error and cannot run. Try again.")
            messagebox.showwarning("Execution Error", f"Error: {programs[choice]} encountered an issue and did not run successfully.")

    elif choice == "5":
        messagebox.showinfo("Placeholder", "This option is not implemented yet.")

    elif choice.lower() in {"bye", "exit"}:
        print("Bye!" if choice == "bye" else "Exiting...")
        break