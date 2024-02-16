def figura(figura, base_o_lado):
    if figura == "Triangulo":
        for i in range(1, base_o_lado + 1):
            espacios = base_o_lado - i
            asteriscos = 2 * i - 1
            print(" " * espacios + "*" * asteriscos)
    
    if figura == "Cuadrado":
        for i in range(base_o_lado):
            print("*" * base_o_lado)

figura("Triangulo", 5)
figura("Cuadrado", 5)
