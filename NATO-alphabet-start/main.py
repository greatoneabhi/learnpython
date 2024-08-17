import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

data = pandas.read_csv("./NATO-alphabet-start/nato_phonetic_alphabet.csv")

phonetic_alphabet_dict = {row.letter: row.code for (index, row) in data.iterrows()}

word = input("Enter a word: ").upper()

phonetic_code_word = [phonetic_alphabet_dict[letter] for letter in word]
print(phonetic_code_word)
