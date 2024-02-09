import time

def sum(num1, num2, seg_a_dormir):
    sumar = num1 + num2
    print(sumar)
    time.sleep(seg_a_dormir)


inicio = time.time()
sum(12, 23, 3)
fin = time.time()
total = fin - inicio
print(f"Tiempo de ejecucion: {total} segundos")
