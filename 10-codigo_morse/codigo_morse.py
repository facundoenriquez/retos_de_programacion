text = "hola pepe"
dict_morse = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '0': '-----', '1': '.----', '2': '..---',
                   '3': '...--', '4': '....-', '5': '.....',
                   '6': '-....', '7': '--...', '8': '---..',
                   '9': '----.'}
text_in_morse = ""

for c in text:
    char = c.upper()
    if char in dict_morse:
        text_in_morse += dict_morse[char]
    else:
        text_in_morse += " "

print(text_in_morse)
