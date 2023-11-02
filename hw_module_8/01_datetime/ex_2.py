# https://plotly.github.io/static/images/dates-time-series-and-timestamp/timeSeriesFormat.png
from datetime import datetime
td = '24.02.2022'
d = datetime.strptime(td, '%d.%m.%Y')
print(type(d))
print(d)
print(d.date())
print(d.time())
print(d.year, d.month, d.day, d.minute)

temp_replace = d.replace(month=5, day=11, minute=15)
print(temp_replace)

str_temp_replace = temp_replace.strftime('%y/%d/%m %H:%M:%S')
print(str_temp_replace)
print(datetime.now().strftime('%Y %B %d'))
