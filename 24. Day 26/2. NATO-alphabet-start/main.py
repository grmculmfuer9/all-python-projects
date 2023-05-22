import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetics = {row.letter: row.code for (index, row) in df.iterrows()}

user_input = input("Enter a word: ")

ans = []
ans = [phonetics[i.upper()] for i in user_input]
print(ans)
