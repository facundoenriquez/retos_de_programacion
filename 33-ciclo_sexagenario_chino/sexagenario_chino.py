def sexagenario(year):
    elementos = ["madera","fuego","tierra","metal","agua"]
    animales = ["rata","buey","tigre","conejo","dragon","serpiente","caballo","oveja","mono","gallo","perro","cerdo"]

    ultimo_ciclo = 1984
    iteracion = year
    iteracion = abs(iteracion-ultimo_ciclo)
    while iteracion > 60:
        iteracion -= 60
    
    for iteration in range(iteracion):
        index = (iteration // 2) % len(elementos)
        elemento = elementos[index]

    for iteration in range(iteracion):
        index = iteration % len(animales)
        animal = animales[index]

    print(f"elemento: {elemento} y animal: {animal}")

sexagenario(1991)