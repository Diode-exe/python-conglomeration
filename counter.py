print("Welcome to the infinite counter! This will make your CPU very warm, depending on your cooling solution.")
number = 0
delay = input("Enter the amount of time to wait before calculating the next number, or press Enter to have no delay: ")
# max = input("Enter the number to stop at, or press Enter to give no limit: ")
ls = input("Enter 1 to overwrite previous lines or press 2 to not: ")
if ls == "1":
    while True:
        number = number + 1
        print(number)
#        if number == max:
#            exit
elif ls == "2":
    while True:
        number = number + 1
        print(number, end="\r", flush=True)
#        if number == max:
#           exit