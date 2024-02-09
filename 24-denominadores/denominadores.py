def maximo_comun_divisor(num1, num2):
    divisores_num1 = []
    length_num1 = range(1, num1+1)
    for i in length_num1:
        if num1 % i == 0:
            divisores_num1.append(i)
    print(divisores_num1)
    divisores_num2 = []
    length_num2 = range(1, num2+1)
    for i in length_num2:
        if num2 % i == 0:
            divisores_num2.append(i)
    print(divisores_num2)
    comunes = [d for d in divisores_num1 if d in divisores_num2]
    mayor = max(comunes)
    print(mayor)

def minimo_comun_multiplo(num1,num2):
    multiplicadores_num1 = []
    div_num1 = 2
    while num1 != 1 and num1 > 0:
        if num1 % div_num1 == 0:
            num1 = num1 / div_num1
            multiplicadores_num1.append(div_num1)
        else:
            div_num1 += 1
    print(multiplicadores_num1)
    multiplicadores_num2 = []
    div_num2 = 2
    while num2 != 1 and num2 > 0:
        if num2 % div_num2 == 0:
            num2 = num2 / div_num2
            multiplicadores_num2.append(div_num2)
        else:
            div_num2 += 1
    print(multiplicadores_num2)
    max_1 = max(multiplicadores_num1)
    max_2 = max(multiplicadores_num2)

maximo_comun_divisor(12, 18)
minimo_comun_multiplo(12,8)