def ortogonal(arr1, arr2):
    if len(arr1) != len(arr2):
        return "Los vectores no son ortogonales"
    else:
        result = (arr1[0] * arr2[0]) + (arr1[1] * arr2[1])
        if result == 0:
            return "Los vectores son ortogonales"
        else:
            return "Los vectores no son ortogonales porque dan distinto de cero"


print(ortogonal([2, -2], [-2, 2]))
print(ortogonal([2, -2], [1, 1]))
