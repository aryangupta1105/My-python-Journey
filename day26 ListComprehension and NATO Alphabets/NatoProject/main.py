import pandas

nato_alphabets = pandas.read_csv("day26 ListComprehension and NATO Alphabets/NatoProject/nato_phonetic_alphabet.csv")
# nato_alphabets.to_dict()s
alpha_dic = {row.letter:row.code for (index, row) in nato_alphabets.iterrows()} 
word = input("Enter a word")
word_list = [alpha_dic[letter.upper()] for letter in word ]
print(word_list)