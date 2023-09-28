"""Функция get_credentials_users из предыдущей задачи возвращает нам список строк username:password:

['andry:uyro18890D', 'steve:oppjM13LL9e']
Реализуйте функцию encode_data_to_base64(data), которая принимает в параметре data указанный список, выполняет кодирование каждой пары username:password в формат Base64 и возвращает список с закодированными парами username:password в виде:

['YW5kcnk6dXlybzE4ODkwRA==', 'c3RldmU6b3Bwak0xM0xMOWU=']"""

import base64


def encode_data_to_base64(data):
    data_base64_list = []
    
    for string in data:
        result = base64.b64encode(string.encode('utf-8')).decode('utf-8')
        data_base64_list.append(result)
        
    return data_base64_list

#   # Перетворити рядок в байти, використовуючи кодування UTF-8
#         bytes_data = string.encode('utf-8')
        
#         # Закодувати байти у форматі Base64
#         result = base64.b64encode(bytes_data).decode('utf-8')
        
#         data_base64_list.append(result)

