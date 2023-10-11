"""Разработайте функцию sanitize_file(source, output), переписывающую в текстовый файл output содержимое текстового файла source, очищенное от цифр.

Требования:

прочтите содержимое файла source, используя менеджер контекста with и режим "r".
запишите новое очищенное от цифр содержимое файла output, используя менеджер контекста with и режим "w"
запись нового содержимого файла output должна быть единоразовая и использовать метод write"""

# def sanitize_file(source, output):
#     try:
#         with open(source, 'r') as source_file, open(output, 'w') as output_file:
#             for line in source_file:
#                 sanitized_line = ''.join(char for char in line if not char.isdigit())
#                 output_file.write(sanitized_line)
#         print(f'Файл {source} був очищений від цифр і збережений у файл {output}')
#     except FileNotFoundError:
#         print(f'Помилка: файл {source} не знайдено.')
        
# source_file = "/home/sergio/Desktop/my python tasks/working_with_files/ingredients.txt"

# output_file = '/home/sergio/Desktop/my python tasks/working_with_files/output.txt' 
# sanitize_file(source_file, output_file)


# def sanitize_file(source, output):
#     with open(source, 'r') as file_1, open(output, 'w') as file_2:
#         for line in file_1:
#             line_1 = ''
#             for char in line:
#                 if not char.isdigit():
#                     line_1 += char
#             file_2.write(line_1)
# source_file = "/home/sergio/Desktop/my python tasks/working_with_files/ingredients.txt"

# output_file = '/home/sergio/Desktop/my python tasks/working_with_files/output.txt' 
# sanitize_file(source_file, output_file)

# def sanitize_file(source, output):
#     with open(source, 'r') as file_1, open(output, 'w') as file_2:
#         for line in file_1:
#             sanitized_line = line.replace('0', '').replace('1', '').replace('2', '').replace('3', '').replace('4', '').replace('5', '').replace('6', '').replace('7', '').replace('8', '').replace('9', '')
#             file_2.write(sanitized_line)
            
def sanitize_file(source, output):
    with open(source, 'r') as file_1, open(output, 'w') as file_2:
        for line in file_1:
            chars_to_remove = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            sanitized_line = line
            for char in chars_to_remove:
                sanitized_line = sanitized_line.replace(char, '')
            file_2.write(sanitized_line)
            
