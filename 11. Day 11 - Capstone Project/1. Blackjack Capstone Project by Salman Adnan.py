# Blackjack Capstone Project
import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
stop = False

def deal_card():
    card = random.choice(cards)
    return card

while not stop:
    print("\033[H\033[J")
    print(logo)
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "n":
        stop = True
        continue
    user_cards = []
    computer_cards = []
    eleven = False
    eleven_count = user_score = computer_score = 0
    
    for _ in range(2):
        card = deal_card()
        user_cards.append(card)
    
    computer_cards.append(deal_card())
    
    if 11 in user_cards:
        eleven = True
        eleven_count = user_cards.count(11)
    
    cards_stop = False
    print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
    print(f"Computer's first card: {computer_cards[0]}")
    
    while not cards_stop:
        if input("Type 'y' to get another card, type 'n' to pass: ") == "n":
            cards_stop = True
            continue
        x = random.choice(cards)
        user_cards.append(x)
        if x == 11:
            eleven = True
            eleven_count += 1
        if eleven == True and sum(user_cards) > 21:
            while eleven_count > 0 and sum(user_cards) > 21:
                user_cards[user_cards.index(11)] = 1
                eleven_count -= 1
            if eleven_count == 0:eleven = False
        print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
        print(f"Computer's first card: {computer_cards[0]}")
        if sum(user_cards) > 21:
            break
    
    while sum(computer_cards) < 17:
        x = random.choice(cards)
        computer_cards.append(x)
        if x == 11:
            eleven = True
            eleven_count += 1
        if eleven == True and sum(computer_cards) > 21:
            while eleven_count > 0 and sum(computer_cards) > 21:
                computer_cards[computer_cards.index(11)] = 1
                eleven_count -= 1
            if eleven_count == 0:eleven = False
        if sum(user_cards) > 21:
             break
    
    user_score = sum(user_cards)
    computer_score = sum(computer_cards)
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    
    if user_score > 21:print("You went over. You lose 😭!")
    elif computer_score > 21:print("Opponent went over. You win 😁!")
    elif user_score > computer_score:print("You win 😁!")
    elif user_score < computer_score:print("You lose 😤!")
    else:print("It's a draw!")
