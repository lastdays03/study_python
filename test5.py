# from my_package import stringutils as su, numberutils as nu, dateutils as du

# print(su.reverse_string("Hello, World!"))
# print(nu.to_money(1000000))
# print(du.to_date("2024-01-01"))
# print(type(du.to_date("2024-01-01")))

# import my_package as mp

# print(mp.stringutils.reverse_string("Hello, World!"))
# print(mp.to_money(1000000))
# print(mp.to_date("2024-01-01"))
# print(type(mp.to_date("2024-01-01")))

import random
import datetime
import calendar

print(random.randint(1, 10))
print(random.choice(range(1, 10)))
print(datetime.date.today())
print(datetime.datetime.now())

day1 = datetime.date(2024, 1, 1)
day2 = datetime.date(2024, 5, 2)
day3 = day2 - day1
print(day3)
print(type(day1))
print(type(day2))
print(type(day3))

cal1 = calendar.month(2024, 1)
print(cal1)
print(type(cal1))
cal2 = calendar.calendar(2024)
print(cal2)
print(type(cal2))
cal3 = calendar.monthrange(2024, 3)
print(cal3)
print(type(cal3))
print(calendar.weekday(2024, 3, 1))

