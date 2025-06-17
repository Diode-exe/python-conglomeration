import os
import time
import platform
import psutil
import shutil
import subprocess
import signal

def ignore_ctrl_c(signum, frame):
    print("\n[!] Ctrl+C is disabled. Use 'shutdown' or 'exit' instead.")

def ctrl_c(signum, frame):
    exit()

signal.signal(signal.SIGINT, ignore_ctrl_c)

version = "1.0"
class pyOS:
    def __init__(self):
        version = "1.0"
        self.services = ["FileSystem", "Shell", "MemoryManager"]

    def boot(self):
        print(f"pyOS v{version} is now running.")
        print("Starting services:")
        for svc in self.services:
            print(f" - {svc}")
        print("\nWelcome to pyOS Terminal!")

def get_cpu_name():
    if platform.system() == "Windows":
        return platform.processor()
    elif platform.system() == "Darwin":
        # macOS
        command = "sysctl -n machdep.cpu.brand_string"
        return subprocess.check_output(command, shell=True).strip().decode()
    elif platform.system() == "Linux":
        with open("/proc/cpuinfo") as f:
            for line in f:
                if "model name" in line:
                    return line.split(":")[1].strip()
    return "Unknown CPU"



def bios_boot_sequence():
    print("PyBIOS v1.03\n")
    time.sleep(1)

    cpu_name = get_cpu_name()
    ram = psutil.virtual_memory()
    total_gb = ram.total / (1024 ** 3)
    total, used, free = shutil.disk_usage("/")

    steps = [
        "[BIOS] Initializing RAM...",
        f"[BIOS] RAM OK: {total_gb:.2f} GB",
        "[BIOS] Detecting CPU...",
        f"[BIOS] CPU OK: {cpu_name}",
        "[BIOS] Checking system bus...",
        "[BIOS] System Bus OK",
        "[BIOS] Scanning storage devices...",
        f"[BIOS] Storage OK: {total / (1024**3):.2f} GB",
        "[BIOS] Loading bootloader...",
    ]
    for step in steps:
        print(step)
        time.sleep(1)

    print("\n[BOOT] PyBoot v1.0")
    print("[BOOT] Boot device: /dev/disk0")
    time.sleep(1)

    print("\n[OS] Loading pyOS Kernel...")
    time.sleep(2)
    print("[OS] Starting system daemons...")
    time.sleep(3)
    print("[OS] Launching shell...")
    time.sleep(0.8)
    print("\nSystem Ready.\n")

    # Optionally: call the real OS now
    osys.boot()

def shutdown_sequence():
    steps = [
        "Shutting down",
        "Stopping daemons",
        "Stopping daemons OK",
        "Unmounting file systems",
        "Unmounting file systems OK",
    ]
    for step in steps:
        print(step)
        time.sleep(1)
    print(f"Exiting pyOS {version}")
    exit()

osys = pyOS()
bios_boot_sequence()



def list_files():
    files = os.listdir(".")
    for file in files:
        print(file)

def change_directory(path):
    try:
        os.chdir(path)
        print(f"Changed directory to {path}")
    except FileNotFoundError:
        print(f"{path} not found.")

def shell():
    path = os.getcwd()
    while True:
        command = input(f"{path} >> ").strip()
        if command == "exit":
            shutdown_sequence()
            break

        elif command == "ls":
            list_files()

        elif command.startswith("cd"):
            path = command[3:].strip()
            if not path:
                path = os.path.expanduser("~")
            change_directory(path)

        elif command == "rename":
            while True:
                selected_file = input("Type the file name to rename: ")
                if os.path.exists(selected_file):
                    new_name = input("Input a new file name: ")
                    os.rename(selected_file, new_name)
                    print(f"Renaming succeeded. {new_name}")
                    break
                else:
                    print("File doesn't exist!")
        
        elif command in ["pwd", "cwd"]:
            cwd = os.getcwd()
            print(cwd)
        
        elif command == "mkdir":
            dirName = input("Directory name to create? ")
            try:
                os.mkdir(dirName)
            except FileExistsError:
                print("The directory already exists!")
        
        elif command == "rm":
            dirName = input("Name of item to remove? ")
            if os.path.isdir(dirName):
                os.rmdir(dirName)
            elif os.path.isfile(dirName):
                os.remove(dirName)
            else:
                print("Item doesn't exist!")

        elif command == "nano":
            os.system("nano")
        
        elif command == "external":
            externalCommand = input("External command? ")
            os.system(externalCommand)
        
        elif command == "help":
            print("Available commands: ls, cd <path>, rename, pwd/cwd, mkdir, rm, nano, external, exit, clear")

        elif command in ["clear", "cls"]:
            if os.name == "posix":
                os.system("clear")  # or "cls" on Windows
            elif os.name("nt"):
                os.system("cls")
        elif command == "shutdown":
            shutdown_sequence()
            break
        elif command == "uptime":
            boot_time = psutil.boot_time()
            uptime_seconds = time.time() - boot_time
            uptime_str = time.strftime("%H:%M:%S", time.gmtime(uptime_seconds))
            print(f"System uptime: {uptime_str}")

        elif command == "crash":
            while True:
                print("!!! SYSTEM FAILURE !!!")
                time.sleep(1)
                print("Error in [UNKNOWN_ERROR]")

                signal.signal(signal.SIGINT, ctrl_c)

        else:
            print(f"Unknown command: {command}")
        

if __name__ == "__main__":
    shell()