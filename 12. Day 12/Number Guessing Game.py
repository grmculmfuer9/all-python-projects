# Number Guessing Game
import random
from art import logo

def guess():
    """Select a number at random between 1 and 100"""
    num = random.randint(1, 100)
    return num

def compare(guess, user_guess):
    """Take guess and user_guess and tell if the number high, low, or same from guess"""
    if user_guess == guess:
        return "same"
    elif user_guess > guess:
        return "Too High"
    return "Too Low"

def attempts(difficulty):
    """Take difficulty level as input and return the number of attempts"""
    if difficulty == "hard":return 5
    return 10

def number_guess_game():
    """Take computer generated guess and attempts left as parameters and prints the result"""
    print("\033[H\033[J")
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    computer_guess = guess()

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    attempts_left = attempts(difficulty)
    
    found_guess = False
    
    while attempts_left > 0 and found_guess == False:
        print(f"You have {attempts_left} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        cmp_guess = compare(computer_guess, user_guess)
        
        if cmp_guess == "same":
            found_guess = True
            continue
        
        print(f"{cmp_guess}\nGuess again.")
        attempts_left -= 1
    
    if found_guess == True:
        print(f"You got it! The answer was {computer_guess}.")
    else:
        print(f"You've run out of guesses, you lose. The actual number was {computer_guess}")

while input("Do you want to play the game? Type 'y' or 'n': ") == "y":
    number_guess_game()
else:
    print("Goodbye")
