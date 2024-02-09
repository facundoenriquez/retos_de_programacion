def conjuntos(arr1, arr2, bool):
    elementos = []
    if bool:
        for t1 in arr1:
            if t1 in elementos:
                pass
            else:
                if t1 in arr2:
                    elementos.append(t1)
    else:
        for t1 in arr1:
            if t1 not in arr2:
                elementos.append(t1)

        for t2 in arr2:
            if t2 not in arr1:
                elementos.append(t2)
    if len(elementos) == 0:
        print("No elements found")
        return elementos
    else:
        return elementos


print(conjuntos(["a", "b", "c", "d"], ["f", "g", "h"], True))
