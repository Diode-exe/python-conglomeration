import string
import time
print("Welcome to the brute forcer (line spam mode)!")
while True:
    try:
        speed = float(input("Choose a speed for Brute Forcing (in seconds, e.g., 0.1 for fast): "))  # Allow floating point input
        if speed <= 0:
            print("Speed must be greater than 0. Please try again.")
            continue
        break  # Exit loop if input is valid
    except ValueError:
        print("Invalid input! Please enter a valid number.")

text = input("Enter String for Brute Force: ")
temp = ' '
for ch in text:
    for i in string.printable:
        print(f"{temp}{i}")  # Line spam effect
        time.sleep(speed)  # Sleep for the user-defined speed
        if i == ch:
            temp += ch
            break
print("\nBrute force complete!")
