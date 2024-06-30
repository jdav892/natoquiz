import pandas

alpha_data = pandas.read_csv("/NATO-alphabet-start/nato_phonetic_alphabet.csv")

alpha_data_frame = pandas.DataFrame(alpha_data)

alpha_dict = {row.letter : row.code for (index, row) in alpha_data_frame.iterrows()}


def generate_phonetic():
    user_input = input("Enter a word ").upper()
    try:
        user_result = [alpha_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonetic()
    else:
        print(user_result)

generate_phonetic()