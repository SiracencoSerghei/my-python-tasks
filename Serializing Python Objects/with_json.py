import json
"""JSON supports the following data types:

record (like a dictionary in Python), the key can only be strings, the values can be any JSON type;
array (like a list in Python);
number (no difference between integers and fractions);
literal(True, False, None);
line."""

# some_data = {'key': 'value', 2: [1, 2, 3], 'tuple': (5, 6), 'a': {'key': 'value'}}
#
# byte_string = json.dumps(some_data)
# unpacked = json.loads(byte_string)
#
# print(unpacked is some_data)    # False
# print(unpacked == some_data)    # False
#
# print(unpacked['key'] == some_data['key'])     # True
# print(unpacked['a'] == some_data['a'] )        # True
# print(unpacked['2'] == some_data[2])           # True
# print(unpacked['tuple'] == [5, 6])             # True

# ==============================

some_data = {'key': 'value', 2: [1, 2, 3], 'tuple': (5, 6), 'a': {'key': 'value'}}
file_name = 'data.json'

with open(file_name, "w") as fh:
    json.dump(some_data, fh)


with open(file_name, "r") as fh:
    unpacked = json.load(fh)


print(unpacked is some_data)    # False
print(unpacked == some_data)    # False

print(unpacked['key'] == some_data['key'])  # True
print(unpacked['a'] == some_data['a'] )     # True
print(unpacked['2'] == some_data[2])        # True
print(unpacked['tuple'] == [5, 6])          # True

"""While executing this code, a data.json file
 appeared in the working folder."""

# ===============================

