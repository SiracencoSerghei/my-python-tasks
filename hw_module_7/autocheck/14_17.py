"""Напишите функцию to_indexed(source_file, output_file), которая будет считывать содержимое файла, добавлять к считанным строкам порядковый номер и сохранять их в таком виде в новом файле.

Каждая строка в созданном файле должна начинаться с ее номера, двоеточия и пробела, после чего должен идти текст строки из исходного файла. Нумерация строк идет от 0."""

def to_indexed(source_file, output_file):
    with open(source_file, 'r') as fh:
        with open(output_file, 'w') as out_fh:
            lines = fh.readlines()
            for i, line in enumerate(lines):
                out_fh.write(f'{i}: {line}')
