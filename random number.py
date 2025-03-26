import random
lives = 3
difficulty = input("Choose difficulty. 1 is 1 to 3, 2 is 1 to 5, and 3 is 1 to 10: ")

if difficulty == "1":
    random_number = random.randint(1, 3)
elif difficulty == "2":
    random_number = random.randint(1, 5)
elif difficulty == "3":
    random_number = random.randint(1, 10)
else:
    print("Invalid difficulty! Exiting...")

while lives > 0:
    try:
        input_number = int(input("Guess the number: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    if random_number == input_number:
        print(f"You win! The number was {random_number}. Exiting...")
        break
    else:
        lives -= 1
        print("Too high!" if input_number > random_number else "Too low!")
        print(f"You currently have {lives} lives left.")

if lives == 0:
    print(f"No more lives! The correct number was {random_number}. Exiting...")