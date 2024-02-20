# calendar del 1 al 24 diciembre 2023
from datetime import datetime


def adeviento(date):
    start_date = "01/12/2023"
    end_date = "24/12/2023"

    start_date_obj = datetime.strptime(start_date, "%d/%m/%Y")
    end_date_obj = datetime.strptime(end_date, "%d/%m/%Y")
    date_obj = datetime.strptime(date, "%d/%m/%Y")

    if start_date_obj <= date_obj <= end_date_obj:
        return "esta dentro"
    elif date_obj > end_date_obj:
        diferencia = date_obj - end_date_obj
        dias = diferencia.days
        horas, remainder = divmod(diferencia.seconds, 3600)
        minutos, _ = divmod(remainder, 60)
        return f"la fecha paso hace {dias} dias con {horas} horas y {minutos} minutos"
    else:
        diferencia = start_date_obj - date_obj
        dias = diferencia.days
        horas, remainder = divmod(diferencia.seconds, 3600)
        minutos, _ = divmod(remainder, 60)
        return f"para la fecha falta {dias} dias con {horas} horas y {minutos} minutos"

print(adeviento("11/11/2023"))
