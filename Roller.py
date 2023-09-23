import random


def main():
    print("How would you like to roll? \n 1. Normal \n 2. With Advantage \n 3. With Disadvantage \n")
    Option = input()
    if Option == "1":
        print("You Rolled", random.randint(1, 20))
    elif Option == "2":
        print("You Rolled", max(random.randint(1, 20), (random.randint(1, 20))), "With Advantage")
    elif Option == "3":
        print("You Rolled", min(random.randint(1, 20), (random.randint(1, 20))),"With Disadvantage")
    else:
        print("Only input numbers 1-3")


main()
