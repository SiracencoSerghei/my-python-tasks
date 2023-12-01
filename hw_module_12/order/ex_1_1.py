import pickle
from time import sleep
from datetime import datetime


class Test:
    def __init__(self, *args):
        self.data = list(args)
        self.saved = None
        self.restored = None

    def __getstate__(self):
        state = self.__dict__.copy()  # self.__dict__ - тут зберігаються всі властивості класу (поля...)
        state['saved'] = datetime.now()
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)  # все що було в self.__dict__ замінити на якийсь state
        self.restored = datetime.now()


if __name__ == "__main__":
    # ==============================
    test = Test(1, 2, 3, 4, 5)
    print(test.data)

    # ==============================
    test_dump = pickle.dumps(test)
    sleep(3)
    test_load = pickle.loads(test_dump)
    print(test.saved, test.restored)
    print(test_load.saved, test_load.restored)