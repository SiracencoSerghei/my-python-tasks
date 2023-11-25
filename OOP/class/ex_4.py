# Сховище з паролем

class KeyStore:
    def __init__(self, name, password):
        self.__password = None
        self.__name = None
        self.__secret = None
        self.name = name
        self.password = password

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def password(self):
        return 'No way to get password'

    @password.setter
    def password(self, value):
        if self.__password is None:
            self.__password = value
        elif self.is_valid():
            self.__password = value

    @property
    def secret(self):
        if self.is_valid():
            return self.__secret

    @secret.setter
    def secret(self, value):
        if self.is_valid():
            self.__secret = value

    def is_valid(self):
        old = input('Please enter the password: ')
        if self.__password == old:
            print("Okay")
            return True
        print('Wrong password')
        return False


k_store = KeyStore('Ivan', '123456')
print(k_store.password)
print(k_store.name)
k_store.name = 'Olga'
print(k_store.name)
k_store.password = '56789'
print(k_store.password)
k_store.secret = 'Hello world'
print(k_store.secret)