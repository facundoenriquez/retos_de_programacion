def ordenar(lista, orden):
    if orden == "Asc":
        ordenado = False
        while not ordenado:
            ordenado = True  # Supongamos que la lista ya está ordenada
            for index in range(len(lista) - 1):
                if lista[index] > lista[index + 1]:
                    # Intercambiar elementos si están en el orden incorrecto
                    lista[index], lista[index +
                                        1] = lista[index + 1], lista[index]
                    ordenado = False  # La lista no está ordenada completamente
    else:
        ordenado = False
        while not ordenado:
            ordenado = True  # Supongamos que la lista ya está ordenada
            for index in range(len(lista) - 1):
                if lista[index] < lista[index + 1]:
                    # Intercambiar elementos si están en el orden incorrecto
                    lista[index], lista[index +
                                        1] = lista[index + 1], lista[index]
                    ordenado = False  # La lista no está ordenada completamente
    return lista


print(ordenar([2, 9, 6, 5, 7, 3], "Asc"))
print(ordenar([2, 9, 6, 5, 7, 3], "Desc"))
