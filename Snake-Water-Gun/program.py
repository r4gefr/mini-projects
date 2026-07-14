import random

tie = 0
win = 0
loss = 0

while True:
    userin = input("Enter 1 for SNAKE, 2 for WATER, 3 for GUN, 0 to quit: ")
    if userin == '0':
        print("Game exited.")
        break
    if userin not in ('1', '2', '3'):
        print("Invalid input! Please enter 1, 2, or 3.")
        continue

    compin = random.randint(1, 3)
    print(f"Computer chose: {compin}")

    if userin == '1':
        if compin == 1:
            print("Both chose SNAKE. It's a tie!")
            tie += 1
        elif compin == 2:
            print("SNAKE drinks WATER. You win!")
            win += 1
        else:
            print("GUN shoots SNAKE. You lose!")
            loss += 1
    elif userin == '2':
        if compin == 1:
            print("SNAKE drinks WATER. You lose!")
            loss += 1
        elif compin == 2:
            print("Both chose WATER. It's a tie!")
            tie += 1
        else:
            print("WATER damages GUN. You win!")
            win += 1
    elif userin == '3':
        if compin == 1:
            print("GUN shoots SNAKE. You win!")
            win += 1
        elif compin == 2:
            print("WATER damages GUN. You lose!")
            loss += 1
        else:
            print("Both chose GUN. It's a tie!")
            tie += 1

    round_score = win - loss
    print(f"Current total -> Wins: {win}, Losses: {loss}, Ties: {tie}, Score: {round_score}\n")
score = win - loss
print(f"Score -> Wins: {win}, Losses: {loss}, Ties: {tie}\n, FINAL SCORE: {score}\n")
