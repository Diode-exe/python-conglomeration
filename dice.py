amountOfDice = int(input("How many dice do you want to roll? "))
dice = []
for i in range(amountOfDice):
    die = int(input("How many sides does the die have? "))
    if die < 1:
        print("The die must have at least 1 side.")
        exit()
    dice.append(die)
import random
def rollDie(sides):
    return random.randint(1, sides)
def rollDice(dice):
    rolls = []
    for die in dice:
        rolls.append(rollDie(die))
    return rolls
def sumRolls(rolls):
    total = 0
    for roll in rolls:
        total += roll
    return total
def printRolls(rolls):
    for i in range(len(rolls)):
        print("Die " + str(i + 1) + ": " + str(rolls[i]))
    print("Total: " + str(sumRolls(rolls)))
def main():
    rolls = rollDice(dice)
    printRolls(rolls)
if __name__ == "__main__":
    main()

