import datetime

year = int(input('enter a year '))
month = int(input('enter a month '))
day = int(input('enter a day '))
year1 = int(input('enter a year '))
month1 = int(input('enter a month '))
day1 = int(input('enter a day '))
date1 = datetime.date(year, month, day)
date2 = datetime.date(year1, month1, day1)
time_diff = date1-date2
print(time_diff)