def bumeran(bumeran):
    total_bumerans = 0
    for i in range(len(bumeran)-2):
        if bumeran[i] == bumeran[i+2]:
            if bumeran[i+1] != bumeran[i]:
                total_bumerans += 1
    return total_bumerans


print(bumeran([2, 1, 2, 3, 3, 4, 2, 4, 2]))
