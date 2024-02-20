def robot(pasos):
    y = True
    steps = {"x": 0, "y": 0}
    giro = -1
    for index, step in enumerate(pasos):
        if index == 0:
            steps["y"] = step
            continue
        if y:
            y = False
            steps["x"] += step * giro
        else:
            y = True
            steps["y"] += step * giro
    return steps


print(robot([10, 5, -2]))
