"""
Клас datetime.timedelta - різниця між двома моментами часу, з точністю до мікросекунд.
"""
from datetime import datetime, timedelta
now = datetime.now()
interval = timedelta(days=5)
result_date = now + interval
print(result_date)

interval = timedelta(days=-15)
result_date = now + interval
print(result_date)