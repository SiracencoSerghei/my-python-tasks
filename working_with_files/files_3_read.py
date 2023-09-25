"""В предыдущей задаче мы записали сотрудников в файл в следующем виде:

Robert Stivenson, 28
Alex Denver, 30
Drake Mikelsson, 19
Выполним теперь обратную задачу и создадим функцию read_employees_from_file(path), которая будет читать данные из файла и возвращать список сотрудников в виде:

['Robert Stivenson, 28', 'Alex Denver, 30', 'Drake Mikelsson, 19']
Помните про присутствие символа конца строки \n при чтении данных из файла. Его необходимо убирать при добавлении прочитанной строки в список (strip).

Требования:

прочтите содержимое файла, используя режим "r".
мы пока не используем менеджер контекста with
верните из функции список сотрудников из файла"""


def read_employees_from_file(path):
    fh = open(path, "r")
    employees_list = []
    
    while True:
        line = fh.readline()
        if not line:
            break
        employees_list.append(line.strip())
    fh.close()   
    return (employees_list)    
    fh.close()
    
path = "/home/sergio/Desktop/my python tasks/working_with_files/employees.txt"

print(read_employees_from_file(path))   
    
    