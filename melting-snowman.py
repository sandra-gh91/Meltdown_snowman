import random

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]

def play_game():
    secret_word = get_random_word()
    guessed_letters = set()
    attempts_left = 6  # number of lives
    word_progress = ["_"] * len(secret_word)

    print("Welcome to Snowman Meltdown!")
    print("The word has", len(secret_word), "letters.")

    while attempts_left > 0 and "_" in word_progress:
        print("\nWord:", " ".join(word_progress))
        print("Attempts left:", attempts_left)
        print("Guessed letters:", " ".join(sorted(guessed_letters)) if guessed_letters else "None")

        guess = input("Guess a letter: ").lower()

        # Validate input
        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print("Good guess!")
            for i, letter in enumerate(secret_word):
                if letter == guess:
                    word_progress[i] = guess
        else:
            print("Wrong guess!")
            attempts_left -= 1

    # End of game
    if "_" not in word_progress:
        print("\n🎉 You won! The word was:", secret_word)
    else:
        print("\n💀 You lost! The word was:", secret_word)

if __name__ == "__main__":
    play_game()
