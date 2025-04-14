import subprocess
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.withdraw()

programs = {
    "1": "brute force.py",
    "2": "random number.py",
    "3": "calculator.py",
    "4": "counter.py",
    "5": "autoclicker launcher.sh",
    "6": "timer launcher.sh",
    "7": "alarm_trigger.py",
    "8": "login.py",
}

while True:
    choice = input("1 for brute forcer (not real hacking tool)\n"
                   "2 for number guessing game\n"
                   "3 to start the calculator\n"
                   "4 to start the infinite counter\n"
                   "5 to start the autoclicker (requires X11)\n"
                   "6 to start the timer/stopwatch\n"
                   "7 to start the alarm clock\n"
                   "8 to login\n"
                   "x to test\n"
                   "type bye or exit to exit: ")

    if choice in programs:
        try:
            path = programs[choice]
            if path.endswith(".sh"):
                subprocess.run(["bash", path], check=True)
            else:
                subprocess.run(["python3", path], check=True)
        except FileNotFoundError:
            print(f"{path} not found!")
            messagebox.showwarning("File Not Found", f"Error: {path} not found!\nMake sure the file exists.")
        except subprocess.CalledProcessError:
            print(f"The program {path} ran into an error.")
            messagebox.showwarning("Execution Error", f"Error: {path} encountered an issue and did not run successfully.")

    elif choice == "x":
        messagebox.showinfo("Placeholder", "This option is not implemented yet.")

    elif choice.lower() in {"bye", "exit"}:
        print("Bye!" if choice == "bye" else "Exiting...")
        break
