# alarm_trigger.py
from datetime import datetime
import subprocess
import time

alarmTime = input("What time should the alarm go off? 24-hour H:M format: ")
alarmName = input("Name your alarm: ")
print("Received. Armed1.")

while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    if current_time == alarmTime:
        print(alarmName)
        subprocess.Popen(["/test-venv/bin/python3", "alarm_player.py"])
        break
    time.sleep(5)
1