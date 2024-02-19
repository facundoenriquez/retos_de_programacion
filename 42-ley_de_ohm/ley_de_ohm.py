def ley_de_ohm(v, r, i):
    if (v == None and r == None) or (v == None and i == None) or (r == None and i == None):
        return "Invalid values"

    if v != None and r != None:
        i = v/r
        return i

    if v != None and i != None:
        r = v/i
        return r

    if r != None and i != None:
        v = r*i
        return v


print(ley_de_ohm(None, 3, 4))
