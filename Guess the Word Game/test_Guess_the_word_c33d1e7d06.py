import unittest
from unittest.mock import patch
from io import StringIO
import random

def choose_random_word():
    words = ["python", "java", "ruby", "javascript"]
    return random.choice(words)

def display_word(word, guessed_letters):
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])

def guess_the_word():
    print("Welcome to Guess the Word game!")
    secret_word = choose_random_word()
    guessed_letters = []
    attempts = 6

    while attempts > 0:
        print(f"\nWord: {display_word(secret_word, guessed_letters)}")
        print(f"Attempts left: {attempts}")
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            if set(guessed_letters) == set(secret_word):
                print("Congratulations! You guessed the word!")
                print(f"The word was: {secret_word}")
                return True
            else:
                print("Correct guess!")
        else:
            attempts -= 1
            print("Incorrect guess!")

    else:
        print("Game over! You ran out of attempts.")
        print(f"The word was: {secret_word}")
        return False

class TestGuessTheWord(unittest.TestCase):

    @patch('builtins.input', side_effect=['p', 'y', 't', 'h', 'o', 'n'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_guess_the_word_success(self, mock_stdout, mock_input):
        random.seed(0)
        self.assertTrue(guess_the_word())
        self.assertIn("Congratulations! You guessed the word!", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['a', 'b', 'c', 'd', 'e', 'f'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_guess_the_word_failure(self, mock_stdout, mock_input):
        random.seed(0)
        self.assertFalse(guess_the_word())
        self.assertIn("Game over! You ran out of attempts.", mock_stdout.getvalue())

if __name__ == "__main__":
    unittest.main()
