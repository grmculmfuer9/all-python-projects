def print_board(lst):
    for x in range(3):
        print("-------------------")
        print("|", lst[x][0], "|", lst[x][1], "|", lst[x][2], "|")
    print("-------------------")


progress_lst = [["   ", "   ", "   "], ["   ", "   ", "   "], ["   ", "   ", "   "]]
print("Welcome to Tic Tac Toe!")
print("Player 1, you are X's")
print("Player 2, you are O's")
print("The board is numbered as follows:")
print(" 1 | 2 | 3 ")
print("-----------")
print(" 4 | 5 | 6 ")
print("-----------")
print(" 7 | 8 | 9 ")
print("-----------")
print("Starting Game...")

player = 2
not_won = True
while not_won:
    player = 1 if player == 2 else 2
    print_board(lst=progress_lst)
    input_element = input(f"Player {player} enter a number (1-9): ")
    if player == 1:
        progress_lst[(int(input_element) - 1) // 3][(int(input_element) % 3) - 1] = " X "
    elif player == 2:
        progress_lst[(int(input_element) - 1) // 3][(int(input_element) % 3) - 1] = " O "
    else:
        print('Wrong Input')

    # Check if player has won
    if (progress_lst[0][0] == progress_lst[0][1] == progress_lst[0][2] == " X ") or (
            progress_lst[1][0] == progress_lst[1][1] == progress_lst[1][2] == " X ") or (
            progress_lst[2][0] == progress_lst[2][1] == progress_lst[2][2] == " X ") or (
            progress_lst[0][0] == progress_lst[1][0] == progress_lst[2][0] == " X ") or (
            progress_lst[0][1] == progress_lst[1][1] == progress_lst[2][1] == " X ") or (
            progress_lst[0][2] == progress_lst[1][2] == progress_lst[2][2] == " X ") or (
            progress_lst[0][0] == progress_lst[1][1] == progress_lst[2][2] == " X ") or (
            progress_lst[0][2] == progress_lst[1][1] == progress_lst[2][0] == " X "):
        print_board(lst=progress_lst)
        print(f"Player {player} has won!")
        not_won = False
