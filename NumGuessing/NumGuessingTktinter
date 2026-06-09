import tkinter as tk
import random

class GuessingGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")

        self.max_number = 100
        self.compin = random.randint(1, self.max_number)
        self.count = 0

        self.label = tk.Label(root, text="Guess a number between 1 and 100")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.button = tk.Button(root, text="Guess", command=self.check_guess)
        self.button.pack(pady=5)

        self.result = tk.Label(root, text="")
        self.result.pack(pady=10)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
        except ValueError:
            self.result.config(text="Enter a valid number")
            return

        self.count += 1

        if guess < self.compin:
            self.result.config(text="Go Higher!")
        elif guess > self.compin:
            self.result.config(text="Go Lower!")
        else:
            self.result.config(
                text=f"Correct! Attempts: {self.count}"
            )

root = tk.Tk()
GuessingGameGUI(root)
root.mainloop()
