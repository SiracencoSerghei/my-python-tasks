"""Реализуйте функцию get_credentials_users(path), которая возвращает список строк из бинарного файла, созданного в предыдущей задаче, где:

path - путь к файлу.
Формат файла:

andry:uyro18890D
steve:oppjM13LL9e
Откройте файл для чтения, используя with и режим rb. Сформируйте список строк из файла и верните его из функции get_credentials_users в следующем формате:

['andry:uyro18890D', 'steve:oppjM13LL9e']
Требования:

Используйте менеджер контекста для чтения из файла"""


def get_credentials_users(path: str) -> list:
    
    users_info = []
    
    with open(path, 'rb') as fh:
        
        for line in fh:
            user = line.strip().decode('utf-8')
            users_info.append(user)
        
    return users_info

print(get_credentials_users('/home/sergio/Desktop/my python tasks/working_with_files/users.txt'))