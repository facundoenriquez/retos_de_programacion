def numeros_perdidos(nums):
    ordenada = True
    numeros_perdidos = []
    for i in range(len(nums) - 1):
        if nums[i] >= nums[i + 1]:
            ordenada = False

    if not ordenada:
        raise ValueError("La lista no esta ordenada")

    for i in range(1, nums[-1]-nums[0]+1):
        if nums[0] + i not in numeros_perdidos and nums[0] + i not in nums:
            numeros_perdidos.append(nums[0]+i)
    print(numeros_perdidos)


numeros_perdidos([-10, 5, 11, 20])
