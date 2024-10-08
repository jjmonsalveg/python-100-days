import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_phonetics = { row.letter: row.code for (_, row) in data.iterrows()}

user_input = input("Enter a word:").upper()
nato_map = [nato_phonetics[letter] for letter in list(user_input)]
print(nato_map)
