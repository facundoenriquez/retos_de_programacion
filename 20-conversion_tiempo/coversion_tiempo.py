def conversor(dias, horas, minutos, segundos):
    # 1 seg = 1000 milisegundos
    dias_a_milisegundos = dias * 24 * (60 ** 2) * 1000
    horas_a_milisegundos = horas * (60 ** 2) * 1000
    minutos_a_milisegundos = minutos * 60 * 1000
    segundos_a_milisegundos = segundos * 1000
    return dias_a_milisegundos, horas_a_milisegundos, minutos_a_milisegundos, segundos_a_milisegundos


print(conversor(2, 3, 4, 5))
