import os

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
            print("Exiting shell.")
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
            if os.name("posix"):
                os.system("clear")  # or "cls" on Windows
            elif os.name("nt"):
                os.system("cls")


        else:
            print(f"Unknown command: {command}")
        

if __name__ == "__main__":
    shell()
