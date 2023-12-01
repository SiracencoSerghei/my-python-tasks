import pickle
from time import sleep


class A:
    def __init__(self, value):
        self.value = value
        self.data = lambda: 5  # cannot be pickled
        self.is_valid = False  # don't want to pickled
        self.text = 'hfdgfhdghdgfhgdhfgdhfd'

    def __getstate__(self):
        return [self.value, self.text]

    def __setstate__(self, state):
        self.value = state[0]
        self.data = lambda: 5
        self.is_valid = False
        self.text = state[1]


a = A('Hello world!')

s = pickle.dumps(a)

a_deserialize = pickle.loads(s)
print(a_deserialize)
print(a_deserialize.value)
print(a_deserialize.data())
print(a_deserialize.is_valid)
print(a_deserialize.text)