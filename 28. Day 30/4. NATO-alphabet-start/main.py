import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetics = {row.letter: row.code for (index, row) in df.iterrows()}


def phonetic_alphabet():
    user_input = input("Enter a word: ").upper()

    try:
        ans = [phonetics[i] for i in user_input]
    except KeyError:
        print("Sorry, only letters are allowed in the alphabet please.")
        phonetic_alphabet()
    else:
        print(ans)


phonetic_alphabet()
