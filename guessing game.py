import tkinter as tk
import random

class GuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        
        self.number_to_guess = random.randint(1, 10)
        self.attempts = 0
        
        self.label = tk.Label(root, text="Guess a number between 1 and 10:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=10)

        self.guess_button = tk.Button(root, text="Guess", command=self.check_guess)
        self.guess_button.pack(pady=10)

        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset_game)
        self.reset_button.pack(pady=10)

    def check_guess(self):
        try:
            player_guess = int(self.entry.get())
            self.attempts += 1
            
            if player_guess < self.number_to_guess:
                self.result_label.config(text="Too low! Try again.")
            elif player_guess > self.number_to_guess:
                self.result_label.config(text="Too high! Try again.")
            else:
                self.result_label.config(text=f"Congratulations! You've guessed the number {self.number_to_guess} in {self.attempts} attempts.")
                self.guess_button.config(state=tk.DISABLED)  # Disable the guess button after winning
        except ValueError:
            self.result_label.config(text="Please enter a valid integer.")

    def reset_game(self):
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0
        self.result_label.config(text="")
        self.entry.delete(0, tk.END)
        self.guess_button.config(state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    game = GuessingGame(root)
    root.mainloop()
