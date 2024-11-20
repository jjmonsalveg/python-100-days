import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(f"{year=} {type(year)}")


date_of_birth = dt.datetime(year=1988, month=12, day=12, hour=4)
print(date_of_birth)