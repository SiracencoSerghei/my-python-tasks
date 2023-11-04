import pickle

# some_data = {
#     (1, 3.5): 'tuple',
#     2: [1, 2, 3],
#     'a': {'key': 'value'}
# }
#
# byte_string = pickle.dumps(some_data)
# unpacked = pickle.loads(byte_string)
#
# print(unpacked == some_data)    # True
# print(unpacked is some_data)    # False

# =========================================

# some_data = {
#     (1, 3.5): 'tuple',
#     2: [1, 2, 3],
#     'a': {'key': 'value'}
# }
#
# file_name = 'data.bin'
#
# with open(file_name, "wb") as fh:
#     pickle.dump(some_data, fh)
#
#
# with open(file_name, "rb") as fh:
#     unpacked = pickle.load(fh)
#
#
# print(unpacked == some_data)    # True
# print(unpacked is some_data)    # False

# ============================

import pickle


class Human:
    def __init__(self, name):
        self.name = name


bob = Human("Bob")
encoded_bob = pickle.dumps(bob)

decoded_bob = pickle.loads(encoded_bob)

result = bob.name == decoded_bob.name
print(result) # True

"""But if you wanted to pass a bob object
 over the network to another computer that
  doesn't know anything about the Human class,
   you'll get an error. If the Human class is
    declared at both ends of the communication
     channel, then such an exchange will work."""

