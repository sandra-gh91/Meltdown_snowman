import random

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

# Snowman ASCII Art stages
STAGES = [
    # Stage 0: Full snowman
    """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     ( : ) 
    """,
    # Stage 1: Bottom part starts melting
    """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
    """,
    # Stage 2: Only the head remains
    """
      ___  
     /___\\ 
     (o o) 
    """,
    # Stage 3: Snowman completely melted
    """
      ___  
     /___\\ 
    """
]

def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]

def display_game_state(mistakes, secret_word, guessed_letters):
    """Displays the current snowman stage and guessed word progress."""
    print(STAGES[mistakes])  # Show snowman based on mistakes
    word_progress = [letter if letter in guessed_letters else "_" for letter in secret_word]
    print("Word:", " ".join(word_progress))
    print("Guessed letters:", " ".join(sorted(guessed_letters)) if guessed_letters else "None")
    print()

def play_game():
    secret_word = get_random_word()
    guessed_letters = set()
    mistakes = 0

    print("Welcome to Snowman Meltdown!")
    print("The word has", len(secret_word), "letters.\n")

    while mistakes < len(STAGES) - 1 and not all(letter in guessed_letters for letter in secret_word):
        display_game_state(mistakes, secret_word, guessed_letters)

        guess = input("Guess a letter: ").lower()

        # Basic validation
        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter!\n")
            continue

        guessed_letters.add(guess)

        if guess not in secret_word:
            mistakes += 1  # Snowman melts

    # End of game
    display_game_state(mistakes, secret_word, guessed_letters)
    if all(letter in guessed_letters for letter in secret_word):
        print("🎉 You won! The word was:", secret_word)
    else:
        print("💀 You lost! The word was:", secret_word)

if __name__ == "__main__":
    play_game()
