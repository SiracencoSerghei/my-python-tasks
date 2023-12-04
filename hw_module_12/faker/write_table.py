from csv import DictWriter
import json
from prettytable import PrettyTable

file_json = 'users.json'
file_csv = 'users.csv'


def get_users():
    with open(file_json) as reader:
        users = json.load(reader)
        return users


def write_table():
    users = get_users()
    with open(file_csv, 'w', encoding='utf-8', newline='') as file:
        fieldsnames = users[0].keys()
        t = PrettyTable(fieldsnames)
        t.align = 'c'
        writer = DictWriter(file, delimiter=';', fieldnames=fieldsnames)
        writer.writeheader()
        for row in users:
            writer.writerow(rowdict=row)
            t.add_row(row.values())
        print("CSV table was created.")
        print(t)


if __name__ == '__main__':
    write_table()
