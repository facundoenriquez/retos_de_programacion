def trap_water(heights):
    n = len(heights)
    
    if n <= 2:
        return 0  # No se puede atrapar agua con menos de 3 bloques
    
    left_max = [0] * n
    right_max = [0] * n
    
    # Calcula la altura máxima a la izquierda de cada posición
    left_max[0] = heights[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], heights[i])
    
    # Calcula la altura máxima a la derecha de cada posición
    right_max[n - 1] = heights[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], heights[i])
    
    trapped_water = 0
    
    # Calcula la cantidad de agua atrapada para cada posición
    for i in range(n):
        trapped_water += max(0, min(left_max[i], right_max[i]) - heights[i])
    
    return trapped_water

# Ejemplo de uso
heights = [4, 0, 3, 6, 1, 3]
result = trap_water(heights)
print(f"La cantidad de agua atrapada es: {result} unidades.")
