INVITED_NAMES_PATH = './Input/Names/invited_names.txt'
NEW_FILES_PATH = "./Output/ReadyToSend/"
PLACEHOLDER = "[name]"
STARTING_LETTER_PATH = "./Input/Letters/starting_letter.txt"

with open(STARTING_LETTER_PATH, 'r') as letter_file:
    letter_template = letter_file.read()

with open(INVITED_NAMES_PATH, 'r') as names_file:
    names = names_file.readlines()

for name in names:
    formated_name = name.strip()
    new_file_name = f"{formated_name}-letter.txt"

    with open(NEW_FILES_PATH + new_file_name, mode="w") as new_file:
        new_file.write(letter_template.replace(PLACEHOLDER, formated_name))
