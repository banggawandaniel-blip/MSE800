import random


class WordGame:
    # Create the game and set the starting values
    def __init__(self):
        self.words = ["python", "variable", "function", "computer", "research"]
        self.word = random.choice(self.words)
        self.guessed = []
        self.lives = 6

    # Show the word with guessed letters and blanks
    def show_word(self):
        display = ""

        for letter in self.word:
            if letter in self.guessed:
                display += letter + " "
            else:
                display += "_ "

        return display

    # Check if the player has guessed the whole word
    def check_win(self):
        for letter in self.word:
            if letter not in self.guessed:
                return False
        return True

    # Run the word guessing game
    def play(self):
        print("Welcome to Word Guessing!")

        while self.lives > 0:
            print("\nWord:", self.show_word())
            print("Lives:", self.lives)

            guess = input("Guess a letter: ").lower()

            # Check if the letter was already guessed
            if guess in self.guessed:
                print("You already guessed that letter.")
                continue

            # Store the guessed letter
            self.guessed.append(guess)

            # Check if the letter is in the word
            if guess in self.word:
                print("Correct!")
            else:
                print("Wrong!")
                self.lives -= 1

            # Check if the player has won
            if self.check_win():
                print("\nCongratulations! You guessed the word!")
                print("Word:", self.word)
                return

        # This happens when the player runs out of lives
        print("\nGame over!")
        print("The word was:", self.word)


# Create a WordGame object and start the game
if __name__ == "__main__":
    game = WordGame()
    game.play()