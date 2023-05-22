with open(file="my_file.txt") as file:
    # Read the content of the file
    contents = file.read()
    print(contents)

with open(file="my_file.txt", mode="a") as file:
    # Write content to the file
    file.write("\nWhere can everyone find him?")

with open(file="new_file.txt", mode="a") as file:
    # Make new file automatically
    file.write("Wow!")
