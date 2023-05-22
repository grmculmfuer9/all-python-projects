# Higher Lower Game
from art import logo, vs
from game_data import data
import random

# Select a random dictionary and make a sentence out of it
def set_sentence():
    """Select a random dictionary and make a sentence out of it."""
    x = random.choice(data)
    if x["description"][0].lower() in ("a", "e", "i", "o", "u"):
        connection = "an"
    else:
        connection = "a"
    sentence = f"{x['name']}, {connection} {x['description']}, from {x['country']}."
    follower_count = x["follower_count"]
    return sentence, follower_count

ans_correct = True
sen1_ans = sen2_ans = False
sen1 = ""
sen2 = ""
score = foll_1 = foll_2 = 0

while ans_correct:
    print("\033[H\033[J")
    print(logo)
    
    # Assign Sentences
    if ans_correct and sen2_ans:
        sen1 = sen2
        foll_1 = foll_2
        sen2, foll_2 = set_sentence()
    else:
        sen1, foll_1 = set_sentence()
        sen2, foll_2 = set_sentence()
    
    while sen1 == sen2:
        sen2, foll_2 = set_sentence()
    
    # See who has more followers
    if foll_2 > foll_1:
        sen2_ans = True
        sen1_ans = False
    elif foll_1 > foll_2:
        sen1_ans = True
        sen2_ans = False
    else:
        continue
    
    if score > 0:
        print(f"You're right! Current score: {score}")
    
    print(f"Compare A: {sen1}")
    print(vs)
    print(f"Compare B: {sen2}")
    ans = input("Who has more followers? Type 'A' or 'B': ")
    
    # Calculation of scores
    if ans.lower() == 'a' and sen1_ans:
        score += 1
    elif ans.lower() == 'b' and sen2_ans:
        score += 1
    else:
        print("\033[H\033[J")
        print(f"Sorry, that's wrong. Final score: {score}")
        ans_correct = False
