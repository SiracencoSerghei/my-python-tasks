"""

"""


from datetime import datetime, timedelta
from zoneinfo import ZoneInfo


data = datetime(year=2023, month=10, day=31)
print(data)
print((data.date()))
now = datetime.now()
print(now)
print(now.today())

td = '24.02.2022'
d = datetime.strptime(td,'%d.%m.%Y')
print(d.date())
print(type(d))
print(d.year, d.month, d.day, d.tzinfo)
temp = d.replace(month=5,day=11, minute=15)
print(temp)
print(type(temp))

str_temp = temp.strftime("%Y/%m/%d")
print(str_temp)
print(type(str_temp))

print(datetime.now().strftime('%Y-%B-%d'))
now1 = datetime.now()
interval = timedelta(days=5)
new_date = now1 + interval
new_date = new_date.strftime('%Y-%B-%d')
print("new date: ", new_date)
print(type(new_date))
first_date = d.timestamp()
print(first_date)

d = datetime.fromtimestamp(first_date)
print(d)
str_d = d.strftime("%Y-%m-%d")
print(type(str_d))
print(str_d)
#
# d = datetime.isoformat(d)
# print(d)
# now = datetime.now()
# iso_date_time = now.isoformat()
# print(iso_date_time)
# iso_timezone = now.isoformat() + now.astimezone().strftime("%Y-%m-%d - (%z)")
# print(iso_timezone)
#




