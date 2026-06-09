import random

while True:
    print("Welcome to the Number Guessing Game! \n")
    print("Enter Difficulty Level:")
    print("Easy ----> Number will be b/w 1 and 50")
    print("Med ----> Number will be b/w 1 and 100")
    print("Hard ----> Number will be b/w 1 and 500")
    while True:
        choice = input("Enter your choice: ").lower()
        if choice == "easy" or choice == "e" or choice == "ez":
            compin = random.randint(1, max_number := 50)
            break
        elif choice in ["med", "medium", "m"]:
            compin = random.randint(1, max_number := 100)
            break
        elif choice in ["hard", "h"]:
            compin = random.randint(1, max_number := 500)
            break
        else:
            print("Invalid choice. Try Again.")
            continue

    count = 0

    while True:
        try:
            userin = int(input(f"Guess a number between 1 and {max_number}: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue
        if userin < 1 or userin > max_number:
            print(f"Please enter a number between 1 and {max_number}.")
            continue
        count += 1
        if userin < compin:
            print("Go Higher!", end=' ')
        elif userin > compin:
            print("Go Lower!", end=' ')
        else:
            print("Congratulations! You've guessed the number!")
            break

        diff = abs(userin - compin)
        percentage_diff = diff / max_number

        if percentage_diff <= 0.02:
            print("Extremely close — you're almost there!")
        elif percentage_diff <= 0.05:
            print("Very close — you're getting there!")
        elif percentage_diff <= 0.10:
            print("Getting warmer.")
        elif percentage_diff <= 0.20:
            print("Not far, keep trying.")
        else:
            print("Far off. Try a bigger change.")

    print(f"You guessed the number in {count} attempt{'s' if count > 1 else ''}!")

    play_again = input("\nDo you want to play again? (y/n): ").lower()
    if play_again in ("y", "yes"):
        break
    elif play_again in ("n", "no"):
        print("Thanks for playing! Goodbye!")
        exit()
    else:
        print("Please enter y or n.")


#-----------BELOW BASIC LOGIC WITHOUT DIFFICULTY LEVELS AND PLAY AGAIN------------

import random

compin = random.randint(1, 100)
print("Welcome to the Number Guessing Game!")
count = 0

while True:
    userin = int(input("Guess a number between 1 and 100: "))
    count += 1
    if userin < compin:
        print("Go Higher!", end=' ')
    elif userin > compin:
        print("Go Lower!", end=' ')
    else:
        print("Congratulations! You've guessed the number!")
        break

    diff = abs(userin - compin)
    if diff <= 2:
        print("Extremely close — you're almost there!")
    elif diff <= 5:
        print("Very close — you're getting there!")
    elif diff <= 10:
        print("Getting warmer.")
    elif diff <= 20:
        print("Not far, keep trying.")
    else:
        print("Far off. Try a bigger change.")

print(f"You guessed the number in {count} attempts!")


