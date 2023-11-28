import csv

with open('names.csv', 'w', newline='\n') as csvfile:  # newline = '\n'
    fieldnames = ['first_name', 'last_name', 'test', 'bool', 'adrress', 'age']  # навза стовпчиків
    # записуємо заголовок
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    # записуємо рядки
    writer.writerow({'first_name': '\tTony', 'last_name': 'Stark', 'age': 35})
    writer.writerow({'first_name': 'Bob', 'last_name': 'Smith', 'age': 15})
    writer.writerow({'first_name': 'Alexsa', 'last_name': 'Smith', 'age': 45, 'bool': True})
