# Написати Contex Manager FileReader, який пише в лог timestamp коли файл був відкритий,
# timestamp, коли файл був закритий, ім'я файлу, і як довго файл був відкритий з точністю до секунд.
from datetime import datetime
from time import sleep


class FileReader:
    log = ''
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super(FileReader, cls).__new__(cls)  # cls - екземпляр класу
        return cls.instance

    def __init__(self, filename):
        self.file = None
        self.opened = False
        self.filename = filename
        self.timestamp = None

    def __enter__(self):
        self.file = open(self.filename, 'r')
        self.opened = True
        self.timestamp = datetime.now().timestamp()
        message = '{:<20}|{:^15}| open \n'.format(self.timestamp, self.filename)
        self.log += message
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.opened:
            self.file.close()
        timestamp_closed = datetime.now().timestamp()
        diff = timestamp_closed - self.timestamp
        message = '{:<20}|{:^15}| closed {:>15}s \n'.format(timestamp_closed, self.filename, diff)
        self.log += message
        self.opened = False


reader = FileReader('test.txt')
with reader as file:
    sleep(2)
    print(file.read())

reader = FileReader('ex_1.py')
with reader as file:
    sleep(1)
    print(file.read())

print(reader.log)
