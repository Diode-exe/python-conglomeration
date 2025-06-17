import random

rps = {
    "rock": 1,
    "paper": 2,
    "scissors": 3,
}

def get_choice_name(number):
    for name, val in rps.items():
        if val == number:
            return name

def main():
    while True:
        while True:
            rps_choice_input = input("Rock Paper Scissors: ").strip().lower()
            if rps_choice_input in rps:
                rps_choice = rps[rps_choice_input]
                break
            else:
                print("Invalid choice!")

        rps_opponent = random.randint(1, 3)
        opponent_choice = get_choice_name(rps_opponent).capitalize()
        print(f"Opponent chose: {opponent_choice}")

        winning_pairs = [(1, 3), (2, 1), (3, 2)]
        if rps_choice == rps_opponent:
            print("You tied! Try again!")
            continue
        elif (rps_choice, rps_opponent) in winning_pairs:
            print("You win!")
        else:
            print("You lose...")

        play_again = input("Play again? ").strip().lower()
        if play_again not in ["yes", "y"]:
            print("Goodbye!")
            break

main()
