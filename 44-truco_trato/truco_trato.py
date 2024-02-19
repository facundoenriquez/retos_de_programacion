import random

sustos_icons = ["🎃","👻","💀","🕷","🕸"]
dulces_icons = ["🍰","🍬","🍡","🍭","🍪","🍫","🧁","🍩"]

def truco_trato(str, persona):
    total_heigth = 0
    if str == "truco":
        sustos = ""
        for p in persona:
            for index, _ in enumerate(p["name"]):
                odd = True if index % 2 == 1 else False
                if odd:
                    sustos += random.choice(sustos_icons)
            even = True if p["age"] % 2 == 0 else False
            if even:
                sustos += "".join(random.sample(sustos_icons, 2))
            total_heigth += p["heigth"]
        cant_altura = total_heigth // 100
        for _ in range(1,cant_altura+1):
            sustos += "".join(random.sample(sustos_icons, 3))
        return sustos
    elif str == "trato":
        dulces = ""
        for p in persona:
            for _ in p["name"]:
                dulces += random.choice(dulces_icons)
            if p["age"] >= 9:
                dulces += "".join(random.sample(dulces_icons, 3))
            else:
                cant_age = p["age"] // 3
                dulces += "".join(random.sample(dulces_icons,cant_age))
            if p["heigth"] >= 150:
                dulces += "".join(random.sample(dulces_icons,6))
            else:
                cant_heigth = (p["heigth"] // 50) * 2
                dulces += "".join(random.sample(dulces_icons,cant_heigth))
        return dulces
    else:
        return f"No es un truco o trato"

print(
    truco_trato("trato", [
        {"name": "Joseluis", "age": 14, "heigth": 170},
        {"name": "Maria", "age": 17, "heigth": 140},
        {"name": "Pepe", "age": 15, "heigth": 165},
    ])
)
