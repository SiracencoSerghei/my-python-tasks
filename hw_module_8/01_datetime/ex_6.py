"""
Метод isoformat() використовується для перетворення об'єкта дати і часу в рядок у форматі ISO 8601,
він має наступний вигляд: YYYY-MM-DDTHH:MM:SS.ssssss
де:
YYYY представляє рік (наприклад, "2023").
MM представляє місяць (наприклад, "10" для жовтня).
DD представляє день (наприклад, "23").
T є роздільником між датою та часом.
HH представляє години (від 00 до 23).
MM представляє хвилини (від 00 до 59).
SS представляє секунди (від 00 до 59).
ssssss представляє мікросекунди (опціонально).
"""
from datetime import datetime
now = datetime.now()
iso_date_time = now.isoformat()
print(iso_date_time)
iso_date_time_timezone = now.isoformat() + now.astimezone().strftime('%z')
print(iso_date_time_timezone)
