import calendar

def get_days_in_years(year):
    count = 0
    years = []
    while count < 30:
        is_leap = calendar.isleap(year)
        if is_leap:
            years.append(year)
            count += 1
    print(years)

get_days_in_years(2024)
