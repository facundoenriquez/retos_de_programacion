def rps(jugadas):
    player_1 = 0
    player_2 = 0
    tie = 0

    for play in jugadas:
        if play[0] == "R" and play[1] == "S":
            player_1 += 1
        if play[0] == "R" and play[1] == "P":
            player_2 += 1
        if play[0] == "P" and play[1] == "R":
            player_1 += 1
        if play[0] == "P" and play[1] == "S":
            player_2 += 1
        if play[0] == "S" and play[1] == "P":
            player_1 += 1
        if play[0] == "S" and play[1] == "R":
            player_2 += 1
        if play[0] == play[1]:
            tie += 1

    if player_1 > player_2:
        return "Gano Player 1"
    elif player_1 < player_2:
        return "Gano Player 2"
    else:
        return "Empate"


print(rps([("R", "S"), ("P", "S"), ("R", "R"), ("P", "R")])
      )
