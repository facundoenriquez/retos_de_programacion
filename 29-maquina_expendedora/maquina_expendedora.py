# monedas 5,10,50,100,200

def maquina(monedas, id_producto):
    monedas_permitidas = [5, 10, 50, 100, 200]
    productos = [
        {"id": 1, "name": "coca-cola", "price": 140},
        {"id": 2, "name": "pepsi", "price": 50},
        {"id": 3, "name": "mountain-dew", "price": 70},
        {"id": 4, "name": "sprite", "price": 40},
        {"id": 5, "name": "seven-up", "price": 130},
    ]

    if all(coin in monedas_permitidas for coin in monedas):
        if not any(producto["id"] == id_producto for producto in productos):
            print("No existe el producto")
        else:
            total = 0
            for moneda in monedas:
                total += moneda
            product_info = next((producto["name"], producto["price"])
                                for producto in productos if producto["id"] == id_producto)
            product_name, price = product_info
            if total < price:
                print(f"No hay suficiente dinero para comprar {product_name}")
            else:
                vuelto = total - price
                print(vuelto)
                devolucion = []
                for m in monedas_permitidas[::-1]:
                    if vuelto >= m:
                        it = vuelto // m
                        for _ in range(it):
                            devolucion.append(m)
                            vuelto -= m
                print(f"Toma tu {product_name} y tu vuelto {devolucion}")
    else:
        print("La moneda no esta permitida")


maquina([5, 200], 1)