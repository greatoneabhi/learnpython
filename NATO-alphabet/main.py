import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv("./NATO-alphabet/nato_phonetic_alphabet.csv")
phonetic_alphabet_dict = {row.letter: row.code for (_, row) in data.iterrows()}


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    try:
        word = input("Enter a word: ").upper()
        phonetic_code_word = [phonetic_alphabet_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(phonetic_code_word)


generate_phonetic()
