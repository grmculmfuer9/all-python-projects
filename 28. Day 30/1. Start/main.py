# FileNotFound

try:
    file = open("a_file.txt")
    a_dict = {"key": "value"}
    print(a_dict["key"])
except FileNotFoundError:
    file = open(file="a_file.txt", mode="w")
    file.write("Something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist")
else:  # Runs when all lines in the try block run
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed")
    # raise KeyError("I made this up")
