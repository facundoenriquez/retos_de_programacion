numeros = range(1, 101)

for n in numeros:
    if n % 3 == 0 and n % 5 == 0:
        print(n, "fizzbuzz.")
        continue
    if n % 3 == 0:
        print(n, "fizz.")
    if n % 5 == 0:
        print(n, "buzz.")