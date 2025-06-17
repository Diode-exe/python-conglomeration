import random

rps = {
    "rock": 1,
    "paper": 2,
    "scissors": 3,
}

while True:
    rps_choice_input = input("Rock Paper Scissors: ").strip().lower()

    if rps_choice_input in rps:
        rps_choice = rps[rps_choice_input]
        break
    else:
        print("Invalid choice!")
    
rps_opponent = random.randint(1, 3)

if rps_choice == rps_opponent:
    print("You tied! Try again!")

elif rps_choice == 1 and rps_opponent == 2:
    print("Paper beats rock! You lose...")

elif rps_choice == 1 and rps_opponent == 3:
    print("Rock beats scissors! You win!")

elif rps_choice == 2 and rps_opponent == 1:
    print("Paper beats rock! You win!")

elif rps_choice == 2 and rps_opponent == 3:
    print("Scissors beats paper! You lose...")

elif rps_choice == 3 and rps_opponent == 1:
    print("Scissors beats rock! You lose..")

elif rps_choice == 3 and rps_opponent == 2:
    print("Scissors beats paper! You win!")

else:
    print("You have ran into an error. Odd. Contact the game dev (Diode-exe on GitHub) to report this issue")