import os
import time
import sys
import psutil
import subprocess
import platform

chosenFunction = input("What would you like the system to do? Type help for options: ")

if chosenFunction in ["sleep", "shutdown"]:
    testingChoice = int(input("1 no testing, 2 testing (choose 1 if unsure): "))
    if testingChoice == 1:
        testing = False
    elif testingChoice == 2:
        testing = True

def computerSleep():
    seconds_until_sleep = 5  # default sleep time (seconds)
    range_top = int(seconds_until_sleep * 10) - 1
    spinner_1 = spinning_cursor()
    spinner_2 = spinning_cursor()

    for _ in range(range_top, 0, -1):
        sys.stdout.write("\r" + next(spinner_1) + " Sleep in " + str(1 + (_ // 10)) + " seconds " + next(spinner_2))
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write("\b")
        sys.stdout.flush()

    sys.stdout.write('\rGoodnight                                 ')
    time.sleep(1)
    sys.stdout.write('\r                                          ')

    if platform.system() == "Darwin":
        cmd = "pmset sleepnow"
    elif platform.system() == "Linux":
        cmd = "systemctl suspend"
    elif platform.system() == "Windows":
        cmd = "rundll32.exe powrprof.dll,SetSuspendState 0,1,0"

    if testing:
        print(f"[TEST MODE] Would run: {cmd}")
    else:
        os.system(cmd)

def computerShutdown():
    seconds_until_shutdown = 5  # default shutdown time (seconds)
    range_top = int(seconds_until_shutdown * 10) - 1
    spinner_1 = spinning_cursor()
    spinner_2 = spinning_cursor()

    for _ in range(range_top, 0, -1):
        sys.stdout.write("\r" + next(spinner_1) + " Shutdown in " + str(1 + (_ // 10)) + " seconds " + next(spinner_2))
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write("\b")
        sys.stdout.flush()

    sys.stdout.write('\rGoodnight                                 ')
    time.sleep(1)
    sys.stdout.write('\r                                          ')

    if psutil.OSX:
        cmd = "sudo shutdown -h now"
    elif psutil.LINUX:
        cmd = "systemctl poweroff"
    elif psutil.WINDOWS:
        cmd = "shutdown /s /t 0"
    else:
        cmd = "echo Unsupported OS. Supported OSes: Linux, OSX (Apple), Windows"

    if testing:
        print(f"[TEST MODE] Would run: {cmd}")
    else:
        os.system(cmd)

def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor

def driveEject():
    if chosenFunction == "eject":
        print("Ejecting optical drive!")
        time.sleep(1)
        try:
            result = subprocess.run(["eject"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if result.returncode != 0:
                print("Failed to eject drive. You may not have an optical drive attached.")
                print(f"stderr: {result.stderr.strip()}")
            elif "eject: unable to eject" in result.stderr.lower():
                print("No ejectable drive found.")
            else:
                print("Optical drive ejected (or at least the command ran without obvious failure).")
        except Exception as e:
            print("An unexpected error occurred while trying to eject the drive.")
            print(str(e))
    else:
        print("Invalid function call to driveEject().")

def installHtopIfMissing(argChoice=""):
    try:
        # Try running htop with `--version` to check if it's installed
        result = subprocess.run(["htop", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            print("htop is already installed. Launching...")
            os.system(f"htop {argChoice}")
        else:
            raise FileNotFoundError  # fallback if version command fails
    except FileNotFoundError:
        print("htop is not installed. Installing...")
        try:
            subprocess.run(["sudo", "apt", "install", "-y", "htop"], check=True)
            print("htop installed. Launching...")
            os.system(f"htop {argChoice}")
        except subprocess.CalledProcessError as e:
            print("Failed to install htop.")
            print(f"Error: {e}")

def installSlIfMissing(argChoice=""):
    try:
        result = subprocess.run(["sl", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            print("sl is already installed. Launching...")
            os.system(f"sl {argChoice}")
        else:
            raise FileNotFoundError
    except FileNotFoundError:
        print("sl is not installed. Installing...")
        try:
            subprocess.run(["sudo", "apt", "install", "-y", "sl"], check=True)
            print("sl installed. Launching...")
            os.system(f"sl {argChoice}")
        except subprocess.CalledProcessError as e:
            print("Failed to install sl.")
            print(f"Error: {e}")



if chosenFunction == "eject":
    driveEject()

elif chosenFunction in ["getLogin", "get Login", "get login", "getlogin"]: 
    login = os.getlogin()
    print(login)

elif chosenFunction == "sleep":
    computerSleep()

elif chosenFunction == "shutdown":
    computerShutdown()

elif chosenFunction == "times":
    times = os.times()
    print(times)

elif chosenFunction == "uptime":
    os.system("uptime")

elif chosenFunction == "htop":
    installHtopIfMissing()

elif chosenFunction == "disk space":
    os.system("df -h")

elif chosenFunction in ["train", "sl"]:
    argChoice = input("Arguments? (type help in the main page for arguments)): ")
    installSlIfMissing(argChoice)

elif chosenFunction in ["help", "h"]:
    print("""
There are a few things you can do:
NOTE: Don't type the quotes around commands
1. Type 'getLogin' or 'getlogin' to see who the current user is.
2. Type 'eject' to eject the optical drive.
3. Type 'sleep' to make the computer sleep (supported OSes: Linux, OSX, Windows - experimental on Windows).
4. Type 'shutdown' to shut down the computer (supported OSes: Linux, OSX, Windows).
5. Type 'times' to see the uptime of the system.
6. Type 'htop' to see system processes (requires password to install) type 'man htop' to see all the arguments (too many to list here)
7. Type 'disk space' to see the disk space of the system
8. Type 'train' or 'sl' to draw a train across the screen (requires password to install) arguments: -a for an accident, -l for little train (cont.)
-F to make it fly, -e to allow Ctrl C interruption
    """)
else:
    print("Invalid command! Exiting...")