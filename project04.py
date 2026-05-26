# Quiz: Create a Python game where the computer secretly chooses a random number between 1 and 50. The player has limited attempts to guess the correct number. After every guess, the program should tell the player whether the guessed number is too high or too low. If the player guesses correctly, display a winning message along with the number of attempts used. If the player fails to guess within the given attempts, display a game over message and reveal the secret number. Try to make the program interactive and clean. After finishing the basic version, challenge yourself by adding difficulty levels, replay option, score system, or hints.
import random
secret_number = random.randint(1, 50)
print("Welcome to the Number Guessing Game!")
guess = int(input("Please enter your guess (between 1 and 50): ").strip())
attemps = 1
while guess != secret_number and attemps < 6:
    guess = int(input("Please enter your guess (between 1 and 50): ").strip())
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number correctly in {attemps} attempts.")
        break
    attemps += 1

if guess != secret_number:
    print(f"Game Over! The secret number was {secret_number}.")