"""Разработайте функцию sanitize_file(source, output), переписывающую в текстовый файл output содержимое текстового файла source, очищенное от цифр.

Требования:

прочтите содержимое файла source, используя менеджер контекста with и режим "r".
запишите новое очищенное от цифр содержимое файла output, используя менеджер контекста with и режим "w"
запись нового содержимого файла output должна быть единоразовая и использовать метод write"""

def sanitize_file(source, output):
    try:
        with open(source, 'r') as source_file, open(output, 'w') as output_file:
            for line in source_file:
                sanitized_line = ''.join(char for char in line if not char.isdigit())
                output_file.write(sanitized_line)
        print(f'Файл {source} був очищений від цифр і збережений у файл {output}')
    except FileNotFoundError:
        print(f'Помилка: файл {source} не знайдено.')
        
source_file = "/home/sergio/Desktop/my python tasks/working_with_files/ingredients.txt"

output_file = '/home/sergio/Desktop/my python tasks/working_with_files/output.txt' 
sanitize_file(source_file, output_file)