numbers = range(1, 101)
primal_numbers = []


def isPrimal(num):
    count = 0
    for i in numbers:
        if num % i == 0 and i > 1 and num > 1:
            count += 1    
    if count == 1:
        return True
    return False


for num in numbers:
    primal = isPrimal(num)
    if primal == True:
        primal_numbers.append(num)

print(primal_numbers)
