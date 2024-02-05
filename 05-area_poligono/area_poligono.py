def area_poligono(poligon):
    if poligon not in ["triangle", "square", "rectangle"]:
        return "not a figure"
    elif poligon == "square":
        return "Area : side * side"
    elif poligon == "triangle":
        return "Area : 1/2 * base * height"
    elif poligon == "rectangle":
        return "Area : length * width"

print(area_poligono("triangle"))
print(area_poligono("square"))
print(area_poligono("pepe"))
print(area_poligono("rectangle"))
