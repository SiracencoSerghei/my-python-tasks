import csv

c_codes = {}
# {код країни: назва країни}
# name_file = 'csv/countries.csv'
# name_file = 'serialize/csv/countries.csv'
name_file = 'countries.csv'


with open(name_file, 'r') as file:
    reader = csv.reader(file)
    for line in reader:
        c_codes[line[0]] = line[1]
    c_codes.pop('Code')

print(c_codes.get('UA'))
print(c_codes)
