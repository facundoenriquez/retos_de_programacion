"""
/*
 * Crea una función que reciba un texto y muestre cada palabra en una línea,
 * formando un marco rectangular de asteriscos.
 * - ¿Qué te parece el reto? Se vería así:
 *   **********
 *   * ¿Qué   *
 *   * te     *
 *   * parece *
 *   * el     *
 *   * reto?  *
 *   **********
 */
"""


def palabras_in_line(text):
    arr = text.split(" ")
    max_length = 0

    for word in arr:
        current_length = len(word)
        if current_length > max_length:
            max_length = current_length

    print("**"+"*"*max_length+"**")
    for word in arr:
        print("*"+" "+word+" "*(max_length-len(word)+1)+"*")
    print("**"+"*"*max_length+"**")

palabras_in_line("¿Que te parece el reto?")
