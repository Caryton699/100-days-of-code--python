# QUIZ:  Create a Python game where the computer secretly chooses a word and the player has limited chances to guess it correctly. After each wrong guess, display a message telling the player the guess was incorrect and show how many attempts are left. If the player guesses the word correctly, display a winning message. If the player uses all attempts, reveal the secret word at the end. Try to make the game interactive and user-friendly using loops, conditions, functions, and input statements. After completing the basic version, challenge yourself by adding features like hints, difficulty levels, score tracking, or a replay option.

print("Welcome to the Word Guessing Game!")
import random
def choose_word():
    words = ["python", "programming", "challenge", "developer", "algorithm"]
    return random.choice(words)

def play_game():
    secret_word = choose_word()
    attempts = 6
    guessed_correctly = False
    
    while attempts > 0 and not guessed_correctly:
        guess = input("Enter your guess: ").lower()
        
        if guess == secret_word:
            guessed_correctly = True
            print("Congratulations! You've guessed the word correctly!")
        else:
            attempts -= 1
            print(f"Incorrect guess. You have {attempts} attempts left.")
    
    if not guessed_correctly:
        print(f"Game over! The secret word was: {secret_word}")

play_game()