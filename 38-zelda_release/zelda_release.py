from datetime import datetime


def zelda_realeses(str_game1, str_game2):
    date_format = "%d/%m/%Y"
    zelda_games = {
        "Tears of the Kingdom": "12/05/2023",
        "Skyward sword": "16/07/2021",
        "Link's Awakening": "20/09/2019",
    }
    date_str1 = zelda_games[str_game1]
    date_str2 = zelda_games[str_game2]
    date1 = datetime.strptime(date_str1, date_format)
    date2 = datetime.strptime(date_str2, date_format)
    print(date1, date2)
    
    days_diff = abs((date2-date1).days)
    years_diff = abs((date2-date1).days // 365)
    print(f"dias: {days_diff}, años: {years_diff}")


zelda_realeses("Tears of the Kingdom", "Link's Awakening")
zelda_realeses("Tears of the Kingdom", "Skyward sword")
