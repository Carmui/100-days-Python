import pandas as pd

#Loop through rows of a data frame
#for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    #pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:

df = pd.read_csv("nato_phonetic_alphabet.csv")
dict = {row.letter:row.code for (index, row) in df.iterrows()}

print(dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Tell me the word: ").upper()
list = [dict[letter] for letter in word]

print(list)



