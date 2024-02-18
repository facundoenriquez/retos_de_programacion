def binario_a_decimal(binario):
    suma = 0
    for index, i in enumerate(binario[::-1]):
        if i == "1":
            suma += 2**index
    print(suma)

binario_a_decimal("1010")
