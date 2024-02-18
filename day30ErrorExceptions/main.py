# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("day30ErrorExceptions/nato_phonetic_alphabet.csv")


phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)
# while KeyError:
#     word = input("Enter a word: ").upper()
#     try:
#         output_list = [phonetic_dict[letter] for letter in word]
#     except KeyError:
#         print("Sorry, on ly letters in the alphabets please!")
#         KeyError = True
#     else:
#         print(output_list)
#         KeyError = False

def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabets please!")
        generate_phonetic()
        # Just like recursion
    else:
        print(output_list)

generate_phonetic()