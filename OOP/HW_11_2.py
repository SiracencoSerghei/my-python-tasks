from datetime import datetime
class Field:
    def __init__(self, value):
        self.__value = None
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value


class Birthday(Field):
    @Field.value.setter
    def value(self, value: str):
        self.__value = datetime.strptime(value, '%Y.%m.%d').date()


class Phone(Field):
    # put your logic here
    @Field.value.setter
    def value(self, value):
        # put your logic here
        pass
