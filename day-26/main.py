import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_phonetics = { row.letter: row.code for (_, row) in data.iterrows()}
ask_for_input = True

while ask_for_input:
    user_input = input("Enter a word:").upper()
    try:
        nato_map = [nato_phonetics[letter] for letter in list(user_input)]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        print(nato_map)
        ask_for_input = False
