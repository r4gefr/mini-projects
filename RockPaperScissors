import random
print("Welcome to Rock, Paper, Scissors Game!")
while True:
    userin = input("\nEnter your choice: \n1 for Rock \n2 for Paper \n3 for Scissors (or 'exit' to quit): ").strip().lower()
    if userin == 'exit':
        print("Thanks for playing! Goodbye!")
        break
    computerin = random.choice(["rock", "paper", "scissors"])
    if userin == "1":
        userin = "rock"
    elif userin == "2":
        userin = "paper"
    elif userin == "3":
        userin = "scissors"
    else:
        print("Invalid input. Please enter 1, 2, 3, or 'exit'.")
        continue
    print(f"You chose: {userin}")
    print(f"Computer chose: {computerin}")
    if userin == computerin:
        print("It's a tie!")
    elif (userin == "rock" and computerin == "scissors") or (userin == "paper" and computerin == "rock") or (userin == "scissors" and computerin == "paper"):
        print("You win!")
    else:
        print("Computer wins!")
    