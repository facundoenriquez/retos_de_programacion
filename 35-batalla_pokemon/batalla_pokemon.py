# tipos: agua, planta, electrico, fuego
# ataques y defensas: 1 - 100

def batalla_pokemon(tipo_ataque, tipo_defensa, ataque, defensa):
    if (tipo_ataque == "agua" and tipo_defensa == "agua") or (tipo_ataque == "agua" and tipo_defensa == "electrico") or (tipo_ataque == "planta" and tipo_defensa == "electrico") or (tipo_ataque == "planta" and tipo_defensa == "fuego") or (tipo_ataque == "electrico" and tipo_defensa == "fuego") or (tipo_ataque == "fuego" and tipo_defensa == "electrico"):
        # neutral
        efectividad = 1
        daño = 50 * (ataque/defensa) * efectividad
    if (tipo_ataque == "agua" and tipo_defensa == "planta") or (tipo_ataque == "electrico" and tipo_defensa == "electrico") or (tipo_ataque == "electrico" and tipo_defensa == "planta") or (tipo_ataque == "fuego" and tipo_defensa == "fuego") or (tipo_ataque == "fuego" and tipo_defensa == "agua"):
        # no es muy efectivo
        efectividad = 0.5
        daño = 50 * (ataque/defensa) * efectividad
    if (tipo_ataque == "agua" and tipo_defensa == "fuego") or (tipo_ataque == "planta" and tipo_defensa == "agua") or (tipo_ataque == "planta" and tipo_defensa == "planta") or (tipo_ataque == "electrico" and tipo_defensa == "agua") or (tipo_ataque == "fuego" and tipo_defensa == "planta"):
        # super efectivo
        efectividad = 2
        daño = 50 * (ataque/defensa) * efectividad
    if efectividad == 0.5:
        text = "Tu ataque no es muy efectivo"
    elif efectividad == 1:
        text = "Tu ataque es neutral"
    else:
        text = "Tu ataque fue super efectivo"
    print(f"{round(daño)} {text}")


batalla_pokemon("agua", "planta", 80, 70)
