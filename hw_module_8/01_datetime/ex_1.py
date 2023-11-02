from datetime import datetime

date = datetime(year=2023, month=10, day=31)
print(date)
date = datetime(year=2023, month=10, day=31, hour=19, minute=37, second=55)
print(date)
print(date.date())
print(date.time())

print(datetime.now())
print(datetime.today())