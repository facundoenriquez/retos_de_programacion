def vocal_mas_repetida(text):
    vocales = ["a", "e", "i", "o", "u"]
    obj = {}
    # text.count cuenta la cantidad de una letra en un texto
    found_vocals = {vocal: text.count(vocal)
                    for vocal in vocales if vocal in text}
    if not found_vocals:
        return False
    vocal_mas_repetida = max(found_vocals.values())
    max_vocales = {vocal: frequency for vocal, frequency in found_vocals.items(
    ) if frequency == vocal_mas_repetida}
    return max_vocales


print(vocal_mas_repetida("dale boke"))
