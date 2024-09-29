import random

# List of words for the game
words = ["python", "hangman", "challenge", "developer", "programming", "computer", "algorithm", "function"]

# Function to select a random word
def get_random_word():
    return random.choice(words)

# Function to display the current state of the word
def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

# Main game function
def play_hangman():
    print("Welcome to the Hangman Challenge!")
    word_to_guess = get_random_word()
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    # Game loop
    while True:
        print(f"\nWord: {display_word(word_to_guess, guessed_letters)}")
        print(f"Incorrect guesses: {incorrect_guesses}/{max_incorrect_guesses}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")

        # Player input
        guess = input("Guess a letter: ").lower()

        # Check if the letter was already guessed
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        # Check if the guess is in the word
        if guess in word_to_guess:
            print(f"Good job! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.")

        # Check if the player has guessed the word
        if all(letter in guessed_letters for letter in word_to_guess):
            print(f"\nCongratulations! You guessed the word: {word_to_guess}")
            break

        # Check if the player has run out of attempts
        if incorrect_guesses >= max_incorrect_guesses:
            print(f"\nYou've run out of guesses! The word was: {word_to_guess}")
            break

# Run the game
if __name__ == "__main__":
    play_hangman()
