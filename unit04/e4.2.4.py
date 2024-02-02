import calendar

date = input("enter a date\n")
day = int(date[:2])
month = int(date[3:5])
year = int(date[6: ])
day_number = calendar.weekday(year, month, day)

day_name = calendar.day_name[day_number]
print(day_name)