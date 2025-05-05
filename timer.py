import time
import keyboard
from playsound import playsound

print("Welcome to the timer!")
mode = input("1 for timer\n2 for stopwatch: ")

if mode == "1":
    print("Timer mode!")
    try:
        countFrom = int(input("Enter the number to count down from: "))
    except ValueError:
        print("That's not a number!")
        exit()

    print("Starting in 3 seconds!")
    time.sleep(3)
    while countFrom > 0:
        print(countFrom)
        countFrom -= 1
        time.sleep(1)
    print("Time's up!")
    playsound("/home/rohan/Documents/python/ding.mp3")

elif mode == "2":
    print("Stopwatch mode!")
    print("Starting in 3 seconds!")
    stopwatchNumber = 0
    time.sleep(3)
    while True:
        stopwatchNumber += 1
        print(stopwatchNumber)
        time.sleep(1)
        if keyboard.is_pressed("q"):
            print(" ")
            print("Exiting stopwatch...")
            break

else:
    print("Invalid mode.")
