"""Мы имеем следующую структуру файла:
60b90c1c13067a15887e1ae1,Tayson,3
60b90c2413067a15887e1ae2,Vika,1
60b90c2e13067a15887e1ae3,Barsik,2
60b90c3b13067a15887e1ae4,Simon,12
60b90c4613067a15887e1ae5,Tessi,5
Каждая запись состоит из трех частей и начинается с новой строки. Например, для первой записи начало 60b90c1c13067a15887e1ae1 — это первичный ключ базы данных MongoDB. Он всегда содержит 12 байт или ровно 24 символа. Дальше мы видим кличку кота Tayson и его возраст 3. Все части записи разделены символом запятая ,

Разработайте функцию get_cats_info(path), которая будет возвращать список словарей с данными кошек в виде:

[
    {"id": "60b90c1c13067a15887e1ae1", "name": "Tayson", "age": "3"},
    {"id": "60b90c2413067a15887e1ae2", "name": "Vika", "age": "1"},
    {"id": "60b90c2e13067a15887e1ae3", "name": "Barsik", "age": "2"},
    {"id": "60b90c3b13067a15887e1ae4", "name": "Simon", "age": "12"},
    {"id": "60b90c4613067a15887e1ae5", "name": "Tessi", "age": "5"},
]
Параметры функции:

path - путь к файлу
Требования:

прочтите содержимое файла, используя режим "r".
мы используем менеджер контекста with
верните из функции список кошек из файла в требуемом формате"""

def get_cats_info(path):
    
    with open(path, "r") as fh:
        cats_list_mongo_db = []
        
        while True:
            line = fh.readline().strip()
            if not line:
                break
            line_parts = line.split(',')
            cats_list_mongo_db.append(
                {
                    "id": line_parts[0],
                    "name": line_parts[1],
                    "age": line_parts[2]
                }
            )
        return cats_list_mongo_db
    
path = "/home/sergio/Desktop/my python tasks/working_with_files/cats_info.txt"
print(get_cats_info(path))
