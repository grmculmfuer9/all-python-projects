# Make mail letters for 10 people
NAME_TO_BE_REPLACED = "[name]"
with open(file="Input/Letters/starting_letter.txt") as file:
    starting_line = file.readline().strip()
    rest = file.read().strip()

with open(file="Input/Names/invited_names.txt") as file:
    all_names = [i.strip() for i in file.readlines()]

for i in all_names:
    file_name = f"{i}.txt"
    first_line = f"{starting_line.replace(NAME_TO_BE_REPLACED, i)}\n\n"
    with open(file=f"Output/ReadyToSend/letter_for_{file_name}", mode="w") as file:
        file.write(first_line)
        file.write(rest)
