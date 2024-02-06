decimal_number = 10
binary_representation = ""

while decimal_number > 0:
    remainder = decimal_number % 2
    binary_representation = str(remainder) + binary_representation
    decimal_number //= 2

print(binary_representation)