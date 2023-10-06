"""Реалізуйте функцію file_operations(path, additional_info, start_pos, count_chars), яка додає додаткову інформацію в файл на шляху path з параметра additional_info, і після цього повертає рядок з позиції start_pos довжиною count_chars.

Вимоги:

функція повинна відкривати файл за допомогою with за шляхом path в режимі додавання інформації
записувати в кінець файлу рядок additional_info
після запису функція має відкрити той самий файл для читання
прочитати та повернути рядок з позиції start_pos завдовжки count_chars за допомогою функції seek.
Важливо: для проходження завдання необхідно використовувати менеджер контексту with, методи seek, write та read."""


def file_operations(path, additional_info, start_pos, count_chars):
    with open(path, "a") as fh:
        fh.write(additional_info + "\n")
    
    with open(path, "r") as fh:
        fh.seek(start_pos) # move to the position in a file from which you want to read data
        return fh.read(count_chars)

# # usage example:
# path = "example.txt"
# additional_info = "Additional info"
# start_pos = 4  # 0-based index, starting from the 5th character
# count_chars = 10

# print(file_operations(path, additional_info, start_pos, count_chars))
