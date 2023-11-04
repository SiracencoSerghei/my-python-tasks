"""An open format for storing tabular data that is
 supported by any editor is the csv format.
  The csv format is, in fact, the same text file, but
  with the condition that all the information in it is
   divided into columns and lines by delimiter characters.
    By default, columns are separated by a comma and rows
    are separated by a newline character.
    But you can use any other combination of characters.

Python supports working with tabular data in csv format.
 For this purpose, the csv package is included in the
 standard delivery."""


import csv


# with open('eggs.csv', 'w', newline='') as fh:
#     spam_writer = csv.writer(fh)
#     spam_writer.writerow(['Spam'] * 5 + ['Baked Beans'])
#     spam_writer.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
#
#
# with open('eggs.csv', newline='') as fh:
#     spam_reader = csv.reader(fh)
#     for row in spam_reader:
#         print(', '.join(row))

# ==========================================

with open('names.csv', 'w', newline='') as fh:
    field_names = ['first_name', 'last_name']
    writer = csv.DictWriter(fh, fieldnames=field_names)
    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})


with open('names.csv', newline='') as fh:
    reader = csv.DictReader(fh)
    for row in reader:
        print(row['first_name'], row['last_name'])

"""The DictWriter and DictReader classes allow you to work with
 table rows as with dictionaries, where column names (the first row)
  are used as keys.

Thus, using Python, you can generate tabular data and import data
 from tables."""