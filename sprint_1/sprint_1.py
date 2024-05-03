import datetime as dt

FORMAT = "%d.%m.%Y"


def get_days_to_birthday(name, date_birthday):
    date_birthday = dt.datetime.strptime(date_birthday, FORMAT).date()
    today = dt.date.today()
    if date_birthday.replace(year=dt.date.today().year) > today:
        days_left = date_birthday.replace(year=today.year) - today
    else:
        days_left = date_birthday.replace(year=today.year + 1) - today
    return f'{name}, до твоего дня рождения осталось дней: {days_left}'


dates = [('Max', '23.04.2003'), ('Alice', '21.03.2009')]

for date in dates:
    print(get_days_to_birthday(date[0], date[1]))
