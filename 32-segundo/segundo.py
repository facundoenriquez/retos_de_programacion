def segundo(nums):
    copy_nums = nums.copy()
    for _ in range(2):
        menor = min(copy_nums)
        copy_nums.remove(menor)
    print(f"El menor numero de {nums} es {menor}")

segundo([888, 500, 400, 700, 8])
