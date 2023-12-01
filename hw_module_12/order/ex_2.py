# Друк та нумерація рядків у текстовому файлі.

import pickle

class TextReader:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(self.filename, encoding='utf-8')
        self.line_count = 0

    def readline(self):
        self.line_count += 1
        line = self.file.readline()
        if not line:
            return None
        if line.endswith('\n'):
            line = line[:-1]  # позбуваємось \n
        return f"{self.line_count}: {line}"

    def __getstate__(self):
        state = self.__dict__.copy()  # self.__dict__ - тут зберігаються всі властивості класу (поля...)
        del state['file']  # Fix for: TypeError: cannot serialize '_io.TextIOWrapper' object
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        file = open(self.filename, encoding='utf-8')
        for _ in range(self.line_count):  # пропускаємо раніше прочитані строки з файлу
            file.readline()
        self.file = file  # зберігаємо файл


if __name__ == "__main__":
    reader = TextReader('text.txt')
    print(reader.readline())  # 1
    print(reader.readline())  # 2
    print(reader.readline())  # 3
    new_reader = pickle.loads(pickle.dumps(reader))  # повинен запамятати коли він був серіалізований
    # і продовжити друкувати текст з того самого місця
    while True:
        line = new_reader.readline()
        if line is None:
            break
        else:
            print(line)

    print('-' * 5)
    print(reader.readline())