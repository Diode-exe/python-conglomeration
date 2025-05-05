import math
from fractions import Fraction
import tkinter as tk
from tkinter import messagebox, simpledialog
import os
import json

def set_mode_1():
    global mode
    mode = 1
    root.destroy()


def set_mode_2():
    global mode
    mode = 2
    root.destroy()


mode = 0
global first_number_func
global second_number_func
global user_input
global first_number_func_is_commit
global second_number_func_is_commit
global choice


root = tk.Tk()
root.title("Mode")
root.geometry("250x100")
tk.Button(root, text="Typing based GUI", command=set_mode_1).pack(pady=5)
tk.Button(root, text="Button based GUI", command=set_mode_2).pack(pady=5)




root.mainloop()
if mode == 1:
    def first_number_func():
        while True:
            try:
                first_number = int(simpledialog.askstring("First number", "First number to calculate?"))
                return first_number
            except ValueError:
                messagebox.showerror("Invalid number", "Invalid number! Please try again")

    def second_number_func():
        while True:
            try:
                second_number = float(simpledialog.askstring("Second number", "Second number to calculate?"))
                return second_number
            except ValueError:
                messagebox.showerror("Invalid number", "Invalid number! Please try again")

    def operation():
        while True:
            global operation_calc
            operation_calc = simpledialog.askstring("Operation", "Operation? +, -, *, /, ** (exponentiation), %, root: ")
            if operation_calc in {"+", "-", "*", "/", "**", "%", "root"}:
                return operation_calc
            else:
                messagebox.showerror("Error", "Invalid operation!")

    # Call and store results
    first_number_func = first_number_func()
    second_number_func = second_number_func()
    operation_calc = operation()

    # Perform calculation
    if operation_calc == "+":
        result = first_number_func + second_number_func
        messagebox.showinfo("Result", f"{result}")

    elif operation_calc == "-":
        result = first_number_func - second_number_func
        messagebox.showinfo("Result", f"{result}")

    elif operation_calc == "*":
        result = first_number_func * second_number_func
        messagebox.showinfo("Result", f"{result}")

    elif operation_calc == "/":
        result = first_number_func / second_number_func
        messagebox.showinfo("Result", f"{result}")


    elif operation_calc == "**":
        result = first_number_func ** second_number_func
        messagebox.showinfo("Result", f"{result}")

    elif operation_calc == "%":
        result = first_number_func * second_number_func / 100
        messagebox.showinfo("Result", f"{result}")

    elif operation_calc in ["root", "square root"]:
        try:
            result = math.sqrt(first_number_func)
            messagebox.showinfo("Result", f"{result}")
        except ValueError:
            messagebox.showerror("Error", "ValueError occurred")
        except TypeError:
            messagebox.showerror("Error", "TypeError occurred")

    else:
        messagebox.showerror("Error", "Program error. Try again.")

if mode == 2:
    global memory
    memory = 0
    current_number_func = 0
    history_index = -1
    history_list = []
    


    user_input = ""
    first_number_func = None
    second_number_func = None
    global val
    val = 0
    first_number_func_is_commit = False
    second_number_func_is_commit = False

    def update_display(value):
        global user_input
        if value == "." and "." in user_input:
            return
        user_input += str(value)

        # Adjust font size based on input length
        max_font_size = 32
        min_font_size = 12
        shrink_factor = 1  # Tweak this to control shrink rate
        length = len(user_input)
        font_size = max(int(max_font_size - length * shrink_factor), min_font_size)

        display_label.config(text=user_input, font=("Arial", font_size))

    
    def clear_display():
        global user_input, val
        global first_number_func, second_number_func
        global first_number_func_is_commit, second_number_func_is_commit

        user_input = ""
        val = 0
        first_number_func = None
        second_number_func = None
        first_number_func_is_commit = False
        second_number_func_is_commit = False
        display_label.config(text="")

    def commit_input():
        global first_number_func
        global second_number_func
        global user_input
        global first_number_func_is_commit
        global second_number_func_is_commit
        global current_number_func

        try:
            if not first_number_func_is_commit:
                first_number_func = float(user_input)
                display_label.config(text=f"First committed: {first_number_func}")
                first_number_func_is_commit = True
                current_number_func = 1
                user_input = ""
            elif not second_number_func_is_commit:
                second_number_func = float(user_input)
                display_label.config(text=f"Second committed: {second_number_func}")
                second_number_func_is_commit = True
                current_number_func = 2
                user_input = ""
                open_window()
            else:
                display_label.config(text="Both numbers committed.")
        except ValueError:
            display_label.config(text="Invalid input!")
        


    # def perform_operation():
    #     while True:
    #         operation_now = simpledialog.askstring("Operation", "What operation would you like to perform? +, -, *, /, **, %, root")
    #         if operation_now in {"+", "-", "*", "/", "**", "%", "root", "stop", "bye", "exit"}:
    #             break
    #         messagebox.showerror("Invalid operation", "Please choose a valid operator.")

    #     # Moved outside loop
    #     try:
    #         if operation_now == "+":
    #             result = first_number_func + second_number_func
    #         elif operation_now == "-":
    #             result = first_number_func - second_number_func
    #         elif operation_now == "*":
    #             result = first_number_func * second_number_func
    #         elif operation_now == "/":
    #             if second_number_func == 0:
    #                 messagebox.showerror("Error", "Cannot divide by zero.")
    #                 return
    #             result = first_number_func / second_number_func
    #         elif operation_now == "**":
    #             result = first_number_func ** second_number_func
    #         elif operation_now == "%":
    #             result = first_number_func * second_number_func / 100
    #         elif operation_now == "root":
    #             result = math.sqrt(first_number_func)
    #         elif operation_now in ["stop", "exit", "bye"]:
    #             exit()

    #         messagebox.showinfo("Result", f"{result}")
    #     except Exception as e:
    #         messagebox.showerror("Error", str(e))

    # def perform_operation_button():
    #     tk.Button(root, text="+", font=("Arial", 18), command=clear_display).grid(row=6, column=0, columnspan=3, pady=10)


    def zero_to_display():
        update_display(0)
    
    def open_window():
        global new_window
        new_window = tk.Toplevel()
        new_window.title("Operators")
        tk.Button(new_window, text="+", font=("Arial", 24), command=lambda: button_operation("+")).pack()
        tk.Button(new_window, text="-", font=("Arial", 24), command=lambda: button_operation("-")).pack()
        tk.Button(new_window, text="*", font=("Arial", 24), command=lambda: button_operation("*")).pack()
        tk.Button(new_window, text="/", font=("Arial", 24), command=lambda: button_operation("/")).pack()
        tk.Button(new_window, text="**", font=("Arial", 24), command=lambda: button_operation("**")).pack()
        tk.Button(new_window, text="%", font=("Arial", 24), command=lambda: button_operation("%")).pack()
        tk.Button(new_window, text="root", font=("Arial", 24), command=lambda: button_operation("root")).pack()
        tk.Button(new_window, text="cancel", font=("Arial", 24), command=lambda: button_operation("cancel")).pack()
        tk.Button(new_window, text="close", font=("Arial", 24), command=lambda: button_operation("close")).pack()

    def button_operation(selection):
        try: 
            if selection == "+":
                result = first_number_func + second_number_func
                messagebox.showinfo("Result", f"{result}")
            elif selection == "-":
                result = first_number_func - second_number_func
                messagebox.showinfo("Result", f"{result}")
            elif selection == "*":
                result = first_number_func * second_number_func
                messagebox.showinfo("Result", f"{result}")
            elif selection == "/":
                if second_number_func == 0:
                    messagebox.showerror("Error", "Cannot divide by zero! Press cancel and try again")
                    return
                result = first_number_func / second_number_func
                messagebox.showinfo("Result", f"{result}")
            elif selection == "**":
                result = first_number_func ** second_number_func
                messagebox.showinfo("Result", f"{result}")
            elif selection == "%":
                result = first_number_func * second_number_func / 100
                messagebox.showinfo("Result", f"{result}")
            elif selection == "root":
                result = math.sqrt(first_number_func)
                messagebox.showinfo("Result", f"{result}")
            elif selection == "cancel":
                new_window.destroy()
            elif selection == "close":
                answer = messagebox.askyesno("Close?", "Are you sure you want to close the calculator?")
                if answer:
                    root.destroy()  # cleaner than exit()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def clear_entry():
        global first_number_func, second_number_func
        global first_number_func_is_commit, second_number_func_is_commit
        global current_number_func, user_input
        if current_number_func == 1:
            first_number_func = 0
            first_number_func_is_commit = False
            user_input = ""
            display_label.config(text="First entry cleared")
        elif current_number_func == 2:
            current_number_func = 1
            second_number_func = 0
            second_number_func_is_commit = False
            user_input = ""
            display_label.config(text="Second entry cleared")

    def close_calc():
        answer = messagebox.askyesno("Close?", "Are you sure you want to close the calculator?")
        if answer:
            root.destroy()  # cleaner than exit()

    choice = None    
    
    global choice_for_func

    def memory_save_type():
        dialog = tk.Toplevel()
        dialog.title("Custom Dialog")
        dialog.grab_set()  # Makes it modal
        def choice_func(choice):
            
            if choice == "result":
                choice_for_func = "result"
            elif choice == "first_number":
                choice_for_func = "first_number"
            elif choice == "second_number":
                choice_for_func = "second_number"

        tk.Label(dialog, text="What to save to memory?", font=("Arial", 14)).pack(pady=10)
        tk.Button(dialog, text="Result", command=lambda: choice("result")).pack(pady=5)
        tk.Button(dialog, text="First number", command=lambda: choice("first_number")).pack(pady=5)
        tk.Button(dialog, text="Second number", command=lambda: choice("second_number")).pack(pady=5)
        # def choice(option):
        #     tk.Button(dialog, text="Result", command=lambda: choice("result")).pack(pady=5)
        #     tk.Button(dialog, text="First number", command=lambda: choice("first_number")).pack(pady=5)
        #     tk.Button(dialog, text="Second number", command=lambda: choice("second_number")).pack(pady=5)

    def save_history():
        entry = {
            "first_number": first_number_func,
            "operation": operation_calc,
            "second_number": second_number_func,
            "result": result
        }

        if os.path.exists("history.json"):
            with open("history.json", "r") as f:
                try:
                    history = json.load(f)
                except json.JSONDecodeError:
                    history = []
        else:
            history = []

        history.append(entry)

        with open("history.json", "w") as f:
            json.dump(history, f, indent=4)


    def load_history():
        import os
        global first_number_func, second_number_func, memory, operation_calc, label
        if not os.path.exists("history.json"):
            label["text"] = "No history found."
            return

        with open("history.json", "r") as f:
            try:
                history = json.load(f)
            except json.JSONDecodeError:
                label["text"] = "History file is corrupt."
                return

        # Restore variables
        first_number_func = history.get("first_number", 0)
        operation_calc = history.get("operation", "")
        second_number_func = history.get("second_number", 0)
        memory = history.get("result", 0)

        # Update label to show restored history
        label["text"] = f"{first_number_func} {operation_calc} {second_number_func} = {memory}"

    def load_history_list():
        global history_list
        if os.path.exists("history.json"):
            with open("history.json", "r") as f:
                try:
                    history_list = json.load(f)
                except json.JSONDecodeError:
                    history_list = []
        else:
            history_list = []


    def show_history_entry(index):
        global first_number_func, second_number_func, memory, operation_calc
        entry = history_list[index]
        first_number_func = entry["first_number"]
        second_number_func = entry["second_number"]
        memory = entry["result"]
        operation_calc = entry["operation"]
        label["text"] = f"{first_number_func} {operation_calc} {second_number_func} = {memory}"

    def on_up(event):
        global history_index
        if history_list:
            history_index = (history_index - 1) % len(history_list)
            show_history_entry(history_index)

    def on_down(event):
        global history_index
        if history_list:
            history_index = (history_index + 1) % len(history_list)
            show_history_entry(history_index)

    # GUI Setup
    root = tk.Tk()
    root.title("Calculator")
    root.bind("<Up>", on_up)
    root.bind("<Down>", on_down)

    
    def key_pressed(event):
        global user_input
        key = event.char
        keysym = event.keysym
        print(f"Key pressed: {event.char}")
        if key.isdigit() or key == ".":
            update_display(key)
        elif keysym == "BackSpace":
            user_input = user_input[:-1]
            display_label.config(text=user_input)
        elif key.lower() == "c":  # clear
            clear_display()
        elif key == "\r":  # Enter key
            commit_input()
            if first_number_func and operation_calc and second_number_func:
                save_history(first_number_func, operation_calc, second_number_func, memory)
        elif key == "\b":
            update_display(key)
        elif event.keysym == "BackSpace":
            update_display(key)
        # Add more as needed


    root.bind("<Key>", key_pressed)    


    display_label = tk.Label(root, text="", font=("Arial", 24))
    display_label.grid(row=0, column=0, columnspan=3, pady=10)

    # Number Buttons
    def sin_func():
        result = math.sin(first_number_func)
        messagebox.showinfo("sin result", f"{result}")
    def cos_func():
        result = math.cos(first_number_func)
        messagebox.showinfo("cos result", f"{result}")
    def tan_func():
        result = math.tan(first_number_func)
        messagebox.showinfo("tan result", f"{result}")

    def add_to_memory():
        global memory, result, choice_for_func
        def memory_add_type():
            dialog = tk.Toplevel()
            dialog.title("Memory editor")
            dialog.grab_set()

            def choice_func(choice):
                nonlocal dialog
                global memory, result, first_number_func, second_number_func
                if choice == "result":
                    try:
                        memory += result
                    except NameError:
                        messagebox.showerror("Memory error", "No result available")
                    except TypeError:
                        messagebox.showerror("Memory error", "No result available, did not save")
                elif choice == "first_number":
                    try:
                        memory += first_number_func
                    except NameError:
                        messagebox.showerror("Memory error", "No first number")
                    except TypeError:
                        messagebox.showerror("Memory error", "First number not defined, press commit first!")
                elif choice == "second_number":
                    try:
                        memory += second_number_func
                    except NameError:
                        messagebox.showerror("Memory error", "No second number")
                    except TypeError:
                        messagebox.showerror("Memory error", "Second number not defined, press commit first!")
                dialog.destroy()
                messagebox.showinfo("Memory Updated", f"Memory now: {memory}")

            tk.Label(dialog, text="Add what to memory?", font=("Arial", 14)).pack(pady=10)
            tk.Button(dialog, text="Result", command=lambda: choice_func("result")).pack(pady=5)
            tk.Button(dialog, text="First number", command=lambda: choice_func("first_number")).pack(pady=5)
            tk.Button(dialog, text="Second number", command=lambda: choice_func("second_number")).pack(pady=5)

        memory_save_type()


    def subtract_from_memory():
        def memory_subtract_type():
            dialog = tk.Toplevel()
            dialog.title("Memory editor")
            dialog.grab_set()

            def choice_func(choice):
                nonlocal dialog
                global memory, result, first_number_func, second_number_func
                if choice == "result":
                    try:
                        memory -= result
                    except NameError:
                        messagebox.showerror("Memory error", "No result available")
                    except TypeError:
                        messagebox.showerror("Memory error", "No result available, did not save")
                elif choice == "first_number":
                    try:
                        memory -= first_number_func
                    except NameError:
                        messagebox.showerror("Memory error", "No first number")
                    except TypeError:
                        messagebox.showerror("Memory error", "First number not defined, press commit first!")
                elif choice == "second_number":
                    try:
                        memory -= second_number_func
                    except NameError:
                        messagebox.showerror("Memory error", "No second number")
                    except TypeError:
                        messagebox.showerror("Memory error", "Second number not defined, press commit first!")
                dialog.destroy()
                messagebox.showinfo("Memory Updated", f"Memory now: {memory}")

            tk.Label(dialog, text="Subtract what from memory?", font=("Arial", 14)).pack(pady=10)
            tk.Button(dialog, text="Result", command=lambda: choice_func("result")).pack(pady=5)
            tk.Button(dialog, text="First number", command=lambda: choice_func("first_number")).pack(pady=5)
            tk.Button(dialog, text="Second number", command=lambda: choice_func("second_number")).pack(pady=5)

    def clear_memory():
        global memory
        memory = 0
        messagebox.showinfo("Memory", f"Memory now: {memory}")
    def recall_memory():
        messagebox.showinfo("Memory", f"Memory now: {memory}")



    tk.Button(root, text="sin", font=("Arial", 15), width=1, height=1, command=sin_func).grid(row=5, column=0)
    tk.Button(root, text="cos", font=("Arial", 15), width=1, height=1, command=cos_func).grid(row=5, column=1)
    tk.Button(root, text="tan", font=("Arial", 15), width=1, height=1, command=tan_func).grid(row=5, column=2)

    tk.Button(root, text="M+", font=("Arial", 15), width=1, height=1, command=lambda: add_to_memory()).grid(row=1, column=3)
    tk.Button(root, text="M-", font=("Arial", 15), width=1, height=1, command=lambda: subtract_from_memory()).grid(row=2, column=3)
    tk.Button(root, text="MC", font=("Arial", 15), width=1, height=1, command=lambda: clear_memory()).grid(row=3, column=3)
    tk.Button(root, text="MR", font=("Arial", 15), width=1, height=1, command=lambda: recall_memory()).grid(row=4, column=3)
    
    for i in range(9):
        row = (i // 3) + 1
        col = i % 3
        tk.Button(root, text=str(i + 1), font=("Arial", 18),
                command=lambda val=i+1: update_display(val)).grid(row=row, column=col, padx=5, pady=5)
        
    tk.Button(root, text="0", font=("Arial", 15), width=1, height=1, command=zero_to_display).grid(row=4, column=1)
    tk.Button(root, text=".", font=("Arial", 15), width=1, height=1, command=lambda: update_display(".")).grid(row=4, column=0)

    # Commit Button
    tk.Button(root, text="Commit", font=("Arial", 18), command=commit_input).grid(row=6, column=0, columnspan=3, pady=10)
    tk.Button(root, text="Clear All", font=("Arial", 18), command=clear_display).grid(row=7, column=0, columnspan=2, pady=10)
    tk.Button(root, text="Clear Entry", font=("Arial", 18), command=clear_entry).grid(row=7, column=2, columnspan=2, pady=10)
    tk.Button(root, text="Close", font=("Arial", 18), command=close_calc).grid(row=8, column=0, columnspan=3, pady=10)

    root.mainloop()