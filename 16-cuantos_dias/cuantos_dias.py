from datetime import datetime


def calcular_dias(date1, date2):
    try:
        datetime_object_1 = datetime.strptime(date1, '%d/%m/%Y')
        datetime_object_2 = datetime.strptime(date2, '%d/%m/%Y')
        difference = (datetime_object_2 - datetime_object_1).days
        return abs(difference)
    except ValueError as e:
        raise ValueError(f"Invalid date format: {e}")


print(calcular_dias("10/01/2024", "25/03/2024"))
