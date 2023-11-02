# Перетворення timestamp в рядок
from datetime import datetime

timestamp = 1625309472.357246
d = datetime.fromtimestamp(timestamp)
print(d)
d_int = datetime.fromtimestamp(int(timestamp))
print(d_int)
str_date = d_int.strftime('%d-%m-%Y, %H:%M:%S')
print(str_date)
