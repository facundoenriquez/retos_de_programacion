def completo_carrera(atleta, pista):
    if len(atleta) != len(pista): 
        print("El corredor no completo toda la carrera")
    else:
        for atleta, obstaculo in zip(atleta, pista):
            if atleta == "run" and obstaculo == "_":
                pass
            if atleta == "jump" and obstaculo == "|":
                pass
            if atleta == "run" and obstaculo == "|":
                pista = pista[:pista.index("|")] + "/" + \
                    pista[pista.index("|") + 1:]
            if atleta == "jump" and obstaculo == "_":
                pista = pista[:pista.index("_")] + "x" + \
                    pista[pista.index("_") + 1:]
        # el slice 
        print(pista[0:0])
        return "/" not in pista and "x" not in pista
            
print(completo_carrera(["run", "jump", "run"], "_|_"))
