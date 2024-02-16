def batallas_en_la_edad_media(razas):
    poder_buenos = 0
    poder_malos = 0

    razas_bondadosas = {
        "pelosos": 1,
        "sureños_buenos": 2,
        "enanos": 3,
        "numenoreanos": 4,
        "elfos": 5,
    }

    razas_malvadas = {
        "sureños_malos": 2,
        "orcos": 2,
        "goblins": 2,
        "huargos": 3,
        "trolls": 5,
    }

    for r in razas:
        raza, cant = r["raza"], r["cant"]
        if raza in razas_bondadosas:
            poder_buenos += razas_bondadosas[raza] * cant
        else:
            poder_malos += razas_malvadas[raza] * cant

    if poder_buenos > poder_malos:
        print("Ganaron los buenos")
    elif poder_malos > poder_buenos:
        print("Ganaron los malos")
    else:
        print("Empataron")


batallas_en_la_edad_media([
    {"raza": "pelosos", "cant": 2},
    {"raza": "sureños_buenos", "cant": 3},
    {"raza": "enanos", "cant": 2},
    {"raza": "orcos", "cant": 2},
    {"raza": "goblins", "cant": 1},
    {"raza": "trolls", "cant": 2},
])
