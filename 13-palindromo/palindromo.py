def palindromo(str):
    lower = str.lower()
    replace = lower.replace(" ","")
    revez = replace[::-1]
    if replace == revez:
        print("True")
    else:
        print("False")


palindromo("neuquen")
palindromo("sakas")
palindromo("pepe")
palindromo("Ana lleva al oso la avellana")
