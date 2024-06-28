import pandas

alpha_data = pandas.read_csv("/NATO-alphabet-start/nato_phonetic_alphabet.csv")

alpha_data_frame = pandas.DataFrame(alpha_data)

alpha_dict = {row.letter : row.code for (index, row) in alpha_data_frame.iterrows()}

user_input = input("Enter a word ").upper()

user_result = [alpha_dict[letter] for letter in user_input]
print(user_result)


        