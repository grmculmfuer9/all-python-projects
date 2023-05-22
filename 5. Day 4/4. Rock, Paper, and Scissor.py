# Rock, Paper, and Scissors
import random as r

cmp_lst = ["rock", "paper", "scissor"]
user_input = input("What do you choose from rock, paper, and scissor, write the word only: ")
choice = r.choice(cmp_lst)

if user_input == choice:
    print(f"It's a draw since both of you got {choice}.")
elif choice == "rock" and user_input == "scissor": # rock scissor
    print(f"You lose since you got {user_input} while the computer got {choice}.")
elif choice == "rock" and user_input == "paper": # rock paper
    print(f"You win since you got {user_input} while the computer got {choice}.")
elif choice == "paper" and user_input == "rock": # paper rock
    print(f"You lose since you got {user_input} while the computer got {choice}.")
elif choice == "paper" and user_input == "scissor":# paper scissor
    print(f"You win since you got {user_input} while the computer got {choice}.")
elif choice == "scissor" and user_input == "paper": # scissor rock
    print(f"You lose since you got {user_input} while the computer got {choice}.")
elif choice == "scissor" and user_input == "rock": # scissor paper
    print(f"You win since you got {user_input} while the computer got {choice}.")
else:
    print(f"Your choice {user_input} is invalid.")
