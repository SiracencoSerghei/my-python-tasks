import csv
# import openpyxl

# with open("eggs.csv") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)
# with open("eggs_2.csv", "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow([1,2,3,4,5])
#     writer.writerow(["a", "b", "c", "d", "e"])
#
# ===========================

with open("names_2.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
        # {'first_name': 'Baked', 'last_name': 'Beans'}
        # {'first_name': 'Lovely', 'last_name': 'Spam'}
        # {'first_name': 'Wonderful', 'last_name': 'Spam'}

with open("names_2.csv", "w", newline="") as file:
    field_names = ['first_name', 'last_name', 'age', 'sex']
    writer = csv.DictWriter(file, delimiter=";", fieldnames=field_names)
    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans', 'age': 25, 'sex': "masculine"})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam', 'age': 35, 'sex': "feminine"})


