import math
import tkinter as tk
from tkinter import messagebox, simpledialog
import os
import json

class CalculatorApp:
    def __init__(self, root):
        self.root = root

        # Initialize variables
        self.user_input = ""
        self.first_number_func = None
        self.second_number_func = None
        self.first_number_func_is_commit = False
        self.second_number_func_is_commit = False
        self.choice = None
        self.memory = 0
        self.val = 0
        self.new_window = None
        self.choice_for_func = None
        self.history_index = -1
        self.history_list = []
        self.operation_calc = ""
        self.result = 0
        self.current_number_func = 0

        # GUI setup
        self.root.title("Calculator")
        self.root.bind("<Up>", self.on_up)
        self.root.bind("<Down>", self.on_down)
        self.root.bind("<Key>", self.key_pressed)

        self.display_label = tk.Label(self.root, text="", font=("Arial", 24))
        self.display_label.grid(row=0, column=0, columnspan=3, pady=10)

        for i in range(9):
            row = (i // 3) + 1
            col = i % 3
            tk.Button(self.root, text=str(i + 1), font=("Arial", 18),
                      command=lambda val=i+1: self.update_display(val)).grid(row=row, column=col, padx=5, pady=5)

        tk.Button(self.root, text="0", font=("Arial", 15), width=1, height=1, command=lambda: self.update_display(0)).grid(row=4, column=1)
        tk.Button(self.root, text=".", font=("Arial", 15), width=1, height=1, command=lambda: self.update_display(".")).grid(row=4, column=0)

        tk.Button(self.root, text="Commit", font=("Arial", 18), command=self.commit_input).grid(row=6, column=0, columnspan=3, pady=10)
        tk.Button(self.root, text="Clear All", font=("Arial", 18), command=self.clear_display).grid(row=7, column=0, columnspan=2, pady=10)
        tk.Button(self.root, text="Clear Entry", font=("Arial", 18), command=self.clear_entry).grid(row=7, column=2, columnspan=2, pady=10)
        tk.Button(self.root, text="Close", font=("Arial", 18), command=self.close_calc).grid(row=8, column=0, columnspan=3, pady=10)

        tk.Button(self.root, text="sin", font=("Arial", 15), width=1, height=1, command=self.sin_func).grid(row=5, column=0)
        tk.Button(self.root, text="cos", font=("Arial", 15), width=1, height=1, command=self.cos_func).grid(row=5, column=1)
        tk.Button(self.root, text="tan", font=("Arial", 15), width=1, height=1, command=self.tan_func).grid(row=5, column=2)

        # Placeholder buttons for memory features
        tk.Button(self.root, text="M+", font=("Arial", 15), width=1, height=1, command=self.ask_to_add).grid(row=1, column=3)
        tk.Button(self.root, text="M-", font=("Arial", 15), width=1, height=1, command=self.ask_to_subtract).grid(row=2, column=3)
        tk.Button(self.root, text="MC", font=("Arial", 15), width=1, height=1, command=self.clear_memory).grid(row=3, column=3)
        tk.Button(self.root, text="MR", font=("Arial", 15), width=1, height=1, command=self.recall_memory).grid(row=4, column=3)

    def update_display(self, value):
        if value == "." and "." in self.user_input:
            return
        self.user_input += str(value)
        font_size = max(12, 32 - len(self.user_input))
        self.display_label.config(text=self.user_input, font=("Arial", font_size))

    def clear_display(self):
        self.user_input = ""
        self.val = 0
        self.first_number_func = None
        self.second_number_func = None
        self.first_number_func_is_commit = False
        self.second_number_func_is_commit = False
        self.display_label.config(text="")

    def clear_entry(self):
        if self.current_number_func == 1:
            self.first_number_func = 0
            self.first_number_func_is_commit = False
            self.user_input = ""
            self.display_label.config(text="First entry cleared")
        elif self.current_number_func == 2:
            self.second_number_func = 0
            self.second_number_func_is_commit = False
            self.user_input = ""
            self.current_number_func = 1
            self.display_label.config(text="Second entry cleared")

    def commit_input(self):
        try:
            value = float(self.user_input)
            if not self.first_number_func_is_commit:
                self.first_number_func = value
                self.first_number_func_is_commit = True
                self.current_number_func = 1
                self.display_label.config(text=f"First committed: {self.first_number_func}")
            elif not self.second_number_func_is_commit:
                self.second_number_func = value
                self.second_number_func_is_commit = True
                self.current_number_func = 2
                self.display_label.config(text=f"Second committed: {self.second_number_func}")
            self.user_input = ""
        except ValueError:
            self.display_label.config(text="Invalid input!")

    def close_calc(self):
        if messagebox.askyesno("Close?", "Are you sure you want to close the calculator?"):
            self.root.destroy()

    def key_pressed(self, event):
        key = event.char
        if key.isdigit() or key == ".":
            self.update_display(key)
        elif event.keysym == "BackSpace":
            self.user_input = self.user_input[:-1]
            self.display_label.config(text=self.user_input)
        elif key.lower() == "c":
            self.clear_display()
        elif key == "\r":
            self.commit_input()

    def on_up(self, event):
        if self.history_list:
            self.history_index = (self.history_index - 1) % len(self.history_list)
            self.show_history_entry(self.history_index)

    def on_down(self, event):
        if self.history_list:
            self.history_index = (self.history_index + 1) % len(self.history_list)
            self.show_history_entry(self.history_index)

    def show_history_entry(self, index):
        entry = self.history_list[index]
        self.first_number_func = entry["first_number"]
        self.second_number_func = entry["second_number"]
        self.memory = entry["result"]
        self.operation_calc = entry["operation"]
        self.display_label.config(text=f"{self.first_number_func} {self.operation_calc} {self.second_number_func} = {self.memory}")

    def sin_func(self):
        if self.first_number_func is not None:
            result = math.sin(math.radians(self.first_number_func))
            result = self.result
            messagebox.showinfo("sin result", f"{result}")

    def cos_func(self):
        if self.first_number_func is not None:
            result = math.cos(math.radians(self.first_number_func))
            messagebox.showinfo("cos result", f"{result}")

    def tan_func(self):
        if self.first_number_func is not None:
            result = math.tan(math.radians(self.first_number_func))
            messagebox.showinfo("tan result", f"{result}")

    def ask_to_add(self):
        self.ask_to_add_window = tk.Toplevel(self.root)  # Instantiate the Toplevel window
        self.ask_to_add_window.title("Add to Memory")

        tk.Button(self.ask_to_add_window, text="Add result", command=self.add_result_to_memory).pack(pady=5)
        tk.Button(self.ask_to_add_window, text="Add first number", command=self.add_first_number_to_memory).pack(pady=5)
        tk.Button(self.ask_to_add_window, text="Add second number", command=self.add_second_number_to_memory).pack(pady=5)
        tk.Button(self.ask_to_add_window, text="Cancel", command=self.ask_to_add_window.destroy).pack(pady=5)

    def ask_to_subtract(self):
        self.ask_to_subtract_window = tk.Toplevel(self.root)  # Instantiate the Toplevel window
        self.ask_to_subtract_window.title("Subtract to Memory")

        tk.Button(self.ask_to_subtract_window, text="Subtract result", command=self.subtract_result_from_memory).pack(pady=5)
        tk.Button(self.ask_to_subtract_window, text="Subtract first number", command=self.subtract_first_number_from_memory).pack(pady=5)
        tk.Button(self.ask_to_subtract_window, text="Subtract second number", command=self.subtract_second_number_from_memory).pack(pady=5)
        tk.Button(self.ask_to_subtract_window, text="Cancel", command=self.ask_to_subtract_window.destroy).pack(pady=5)

    def button_operation(selection, self):
        try: 
            if selection == "+":
                result = self.first_number_func + self.second_number_func
                messagebox.showinfo("Result", f"{result}")
            elif selection == "-":
                result = self.first_number_func - self.second_number_func
                messagebox.showinfo("Result", f"{result}")
            elif selection == "*":
                result = self.first_number_func * self.second_number_func
                messagebox.showinfo("Result", f"{result}")
            elif selection == "/":
                if self.second_number_func == 0:
                    messagebox.showerror("Error", "Cannot divide by zero! Press cancel and try again")
                    return
                result = self.first_number_func / self.second_number_func
                messagebox.showinfo("Result", f"{result}")
            elif selection == "**":
                result = self.first_number_func ** self.second_number_func
                messagebox.showinfo("Result", f"{result}")
            elif selection == "%":
                result = self.first_number_func * self.second_number_func / 100
                messagebox.showinfo("Result", f"{result}")
            elif selection == "root":
                result = math.sqrt(self.first_number_func)
                messagebox.showinfo("Result", f"{result}")
            elif selection == "cancel":
                self.new_window.destroy()
            elif selection == "close":
                answer = messagebox.askyesno("Close?", "Are you sure you want to close the calculator?")
                if answer:
                    self.root.destroy()  # cleaner than exit()
        except Exception as e:
            messagebox.showerror("Error", str(e))


    def open_window(self):
        self.new_window = tk.Toplevel()
        self.new_window.title("Operators")
        tk.Button(self.new_window, text="+", font=("Arial", 24), command=lambda: self.button_operation("+")).pack()
        tk.Button(self.new_window, text="-", font=("Arial", 24), command=lambda: self.button_operation("-")).pack()
        tk.Button(self.new_window, text="*", font=("Arial", 24), command=lambda: self.button_operation("*")).pack()
        tk.Button(self.new_window, text="/", font=("Arial", 24), command=lambda: self.button_operation("/")).pack()
        tk.Button(self.new_window, text="**", font=("Arial", 24), command=lambda: self.button_operation("**")).pack()
        tk.Button(self.new_window, text="%", font=("Arial", 24), command=lambda: self.button_operation("%")).pack()
        tk.Button(self.new_window, text="root", font=("Arial", 24), command=lambda: self.button_operation("root")).pack()
        tk.Button(self.new_window, text="cancel", font=("Arial", 24), command=lambda: self.button_operation("cancel")).pack()
        tk.Button(self.new_window, text="close", font=("Arial", 24), command=lambda: self.button_operation("close")).pack()



    def add_result_to_memory(self):
        self.memory += self.result
        messagebox.showinfo("Memory", f"Memory now: {self.memory}")

    def add_first_number_to_memory(self):
        try:
            self.memory += self.first_number_func
            messagebox.showinfo("Memory", f"Memory now: {self.memory}")
        except TypeError:
            messagebox.showerror("Memory error", "Memory error. You probably didn't commit a first number.")
    
    def add_second_number_to_memory(self):
        try:
            self.memory += self.second_number_func
            messagebox.showinfo("Memory", f"Memory now: {self.memory}")
        except TypeError:
            messagebox.showerror("Memory error", "Memory error. You probably didn't commit a second number.")

    def subtract_result_from_memory(self):
        try:
            self.memory -= self.result
            messagebox.showinfo("Memory", f"Memory now: {self.memory}")
        except TypeError:
            messagebox.showerror("Memory error", "Memory error. You probably didn't calculate a result.")

    def subtract_first_number_from_memory(self):
        try:
            self.memory -= self.first_number_func
            messagebox.showinfo("Memory", f"Memory now: {self.memory}")
        except TypeError:
            messagebox.showerror("Memory error", "Memory error. You probably didn't commit a first number.")

    def subtract_second_number_from_memory(self):
        try:
            self.memory -= self.second_number_func
            messagebox.showinfo("Memory", f"Memory now: {self.memory}")
        except TypeError:
            messagebox.showerror("Memory error", "Memory error. You probably didn't commit a second number.")

    def clear_memory(self):
        self.memory = 0
        messagebox.showinfo("Memory", f"Memory now: {self.memory}")

    def recall_memory(self):
        messagebox.showinfo("Memory", f"Memory now: {self.memory}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
