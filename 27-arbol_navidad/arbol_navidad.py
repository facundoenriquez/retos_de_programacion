def arbol(estrellas):
    for i in range(1,estrellas+1,2):
        print(" " * estrellas + "*" * i)
        estrellas -= 1

arbol(7)
