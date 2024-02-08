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
                # print(pista.index("|"))
                print(pista[1:2])
                pista = pista[:pista.index("|")] + "/" + \
                    pista[pista.index("|") + 1:]
            if atleta == "jump" and obstaculo == "_":
                pista = pista[:pista.index("_")] + "x" + \
                    pista[pista.index("_") + 1:]
            # print(pista)
completo_carrera(["run", "jump", "run"], "|_|")
