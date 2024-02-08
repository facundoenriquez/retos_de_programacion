def first_letter_upper(str):
    list_of_letters = [s for s in str]
    list_of_letters[0] = list_of_letters[0].upper()
    join_letters = "".join(list_of_letters)
    print(join_letters)

first_letter_upper("viva peronia!")
