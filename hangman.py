import random

# Lista e fjalëve për lojën
word_list = ["python", "programming", "developer", "software", "engineer", "hangman"]

# Funksioni për të zgjedhur një fjalë rastësisht
def choose_word(word_list):
    return random.choice(word_list)

# Funksioni për të shfaqur fjalën me shkronjat e gjetura
def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

# Funksioni për të vizualizuar "Hangman"
def display_hangman(attempts):
    stages = [
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        ---------
        """,
        """
           -----
           |   |
               |
               |
               |
               |
        ---------
        """
    ]
    return stages[6 - attempts]

# Funksioni kryesor i lojës
def hangman():
    print("Welcome to Hangman!")
    print("Try to guess the word before the man is fully hanged!")
    word = choose_word(word_list)
    guessed_letters = set()
    attempts = 6  # Numri maksimal i tentativave

    while attempts > 0:
        print("\n" + display_hangman(attempts))
        print("\nWord to guess: ", display_word(word, guessed_letters))
        print(f"Remaining attempts: {attempts}")
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again!")
        elif guess in word:
            guessed_letters.add(guess)
            print("Correct guess!")
        else:
            guessed_letters.add(guess)
            attempts -= 1
            print("Wrong guess!")

        if set(word) <= guessed_letters:
            print("\nCongratulations! You guessed the word:", word)
            print("You saved the man! 🎉")
            break
    else:
        print("\n" + display_hangman(attempts))
        print("Game over! The word was:", word)
        print("The man is hanged. Better luck next time! 😢")

# Fillimi i lojës
if __name__ == "__main__":
    hangman()
