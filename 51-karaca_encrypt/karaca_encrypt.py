def karaca(text, isKaraca):
    vocals = {
        "a": 0,
        "e": 1,
        "i": 2,
        "o": 3,
        "u": 4,
    }

    if not isKaraca:
        text_lower = text.lower()
        reverse = text_lower[::-1]
        new_text = ""

        for char in reverse:
            if char in vocals.keys():
                new_text += str(vocals[char])
            else:
                new_text += char
        return new_text+"aca"
    else:
        text_lower = text.lower()
        reverse = text_lower[::-1]
        without_aca = reverse[3:]
        decoded_text = ""

        for char in without_aca:
            if char.isdigit():
                # next te devuelve los items simples de la iteracion sin list ni diccionarios
                decoded_text += next(key for key, value in vocals.items() if value == int(char))
            else:
                decoded_text += char
        return decoded_text


print(karaca("no hay plata", False))
print(karaca("0t0lp y0h 3naca", True))
