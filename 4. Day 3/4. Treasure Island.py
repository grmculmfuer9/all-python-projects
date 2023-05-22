# Treasure Island
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
s = input("Left or Right?\n")
if s.lower() == "left":
    s = input("Swim or Wait?\n")
    if s.lower() == "wait":
        s = input("Which door?\n")
        if s.lower() == "yellow":print("You Win!")
        elif s.lower() == "red":print("Burned by fire.\nGame Over!")
        elif s.lower() == "blue":print("Eaten by Beasts.\nGame Over!")
        else:print("Game Over!")
    else:print("Attacked by trout.\nGame Over!")
else:print("Fall into the hole.\nGame Over!")
