import random
import os
from hangman_words import word_list
from hangman_art import logo, stages


def clear_screen():
    if 'TERM' in os.environ:
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
    else:
        print("\n" * 100)  # Fall back to printing newlines


def hangman():
    """Run the Hangman game."""
    end_of_game = False
    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)
    lives = 6

    print(logo)

    # Create blanks
    display = ["_" for _ in range(word_length)]
    guessed_letters = []

    while not end_of_game:
        guess = input("Guess a letter: ").lower()

        clear_screen()

        if guess in guessed_letters:
            print(f"You've already guessed {guess}")
        else:
            guessed_letters.append(guess)

            if guess in chosen_word:
                for position in range(word_length):
                    letter = chosen_word[position]
                    if letter == guess:
                        display[position] = letter
            else:
                print(f"You guessed {guess}, that's not in the word. You lose a life.")
                lives -= 1
                if lives == 0:
                    end_of_game = True
                    print("You lose.")
                    print(f"The word was: {chosen_word}")

        print(f"{' '.join(display)}")

        if "_" not in display:
            end_of_game = True
            print("You win.")

        print(stages[lives])


if __name__ == "__main__":
    hangman()
