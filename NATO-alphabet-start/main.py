import pandas

# TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}

alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
code_words = {row.letter: row.code for (index, row) in alphabet.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.


user_word = input("Enter a word: ").upper()
name_list = [code_words[letter] for letter in user_word]
print(name_list)
