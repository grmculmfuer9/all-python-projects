# Treasure Map
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
main_map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure, write it like this: column row?\n")
column = int(position[0]) - 1
row = int(position[-1]) - 1
main_map[row][column] = "x"

for i in main_map:
    print()
