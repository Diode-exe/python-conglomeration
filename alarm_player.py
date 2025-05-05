# alarm_player.py
from playsound import playsound
import time

print("Alarm is going off. Press Ctrl+C to stop.")
while True:
    playsound("ding.mp3")
    time.sleep(1)
