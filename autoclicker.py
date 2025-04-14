from pynput.mouse import Button, Controller as MouseController
from pynput import keyboard
import time

mouse = MouseController()
clicking = True

def on_press(key):
    global clicking
    try:
        if key.char == 'q':
            clicking = False
            return False  # Stop the listener
    except AttributeError:
        pass

# Ask the user how to run the clicker
while True:
    readMouse = input("Press 1 to just run, or 2 to print the mouse position and run: ")
    if readMouse in {"1", "2"}:
        break
    print("Invalid selection. Try again.")

# Ask how many clicks to do
amountOfClicks = input("Choose the amount of times to click, or press Enter to infinitely click: ")

# Convert amountOfClicks to an integer, if provided
clicks = None
if amountOfClicks.strip():
    try:
        clicks = int(amountOfClicks)
    except ValueError:
        print("That's not a number! Exiting.")
        exit()

print("Giving you 5 seconds to switch windows... (Press 'q' anytime to quit later)")
time.sleep(5)

def click_loop(print_position=False, max_clicks=None):
    global clicking
    count = 0

    with keyboard.Listener(on_press=on_press):
        while clicking:
            if print_position:
                print(f"Mouse at: {mouse.position}")
            mouse.press(Button.left)
            mouse.release(Button.left)
            time.sleep(0.05)
            if max_clicks is not None:
                count += 1
                if count >= max_clicks:
                    break

# Run based on user input
click_loop(print_position=(readMouse == "2"), max_clicks=clicks)
