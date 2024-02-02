first_numbers = range(50)
serie = []
for index, num in enumerate(first_numbers):
    if index == 0:
        serie.append(0)
        continue
    if index == 1:
        serie.append(1)
        continue
    serie.append(serie[index - 2] + serie[index - 1])
print(serie)