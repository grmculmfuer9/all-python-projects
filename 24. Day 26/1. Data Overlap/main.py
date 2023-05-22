file_1 = []
with open(file="file1.txt") as file:
    file_1 = [int(x.strip()) for x in file.readlines()]

file_2 = []
with open(file="file2.txt") as file:
    file_2 = [int(x.strip()) for x in file.readlines()]

result = []

for x in file_1:
    if x in file_2:
        result.append(x)

print(result)
