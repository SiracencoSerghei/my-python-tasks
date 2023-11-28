# Зберегти у файлі таблицю квадратів та кубів цілих чисел від 1 до 20
name = 'table.csv'
import csv

with open(name, 'w') as file:
    writer = csv.writer(file)
    for item in range(1, 100):
        writer.writerow([item, item ** 2, item ** 3])

with open(name, 'r') as file:
    reader = csv.reader(file)
    res = []
    for line in reader:
        res.append(line)
print(res)
