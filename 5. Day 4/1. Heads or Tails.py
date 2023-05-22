# Heads or Tails
#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
import random
#Write the rest of your code below this line 👇
user_choice = input("Select one: Heads or tails?\n")
computer_choice = random.choice(["Heads", "Tails"])
if user_choice == computer_choice:print(f"You win, both got {user_choice}")
else:print(f"You lose, you got {user_choice} while the computer got {computer_choice}")

