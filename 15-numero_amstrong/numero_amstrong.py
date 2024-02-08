def amstrong_number(num):
    string_numbers = str(num)
    list_of_digits = [digits for digits in string_numbers]
    length = len(list_of_digits)
    sum = 0
    for item in list_of_digits:
        sum += int(item)**length
    if num == sum:
        print("es un numero amstrong")
    else:
        print("no es un numero amstrong")

amstrong_number(153)
