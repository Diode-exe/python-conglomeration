from datetime import datetime
from playsound import playsound
import time
import keyboard
alarmTime = input("What time should the alarm go off? 24 hour H:M format, please,: ")
alarmName = input("Name your alarm")
print("Received. Armed.")
while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    if current_time == alarmTime:
        while True:
            playsound("/home/rohan/Documents/python/ding.mp3")
            time.sleep(1)
            if keyboard.is_pressed("q"):
                False