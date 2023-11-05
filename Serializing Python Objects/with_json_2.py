import json

# some_data = {'key': 'value', "name": "Jack", "age": 21, "brothers": ["Mark", "Mike"]}
#
# ser = json.dumps(some_data)
# print(ser)
# print(type(ser))
# des = json.loads(ser)
# print(des)
# print(type(des))
# print(some_data == des) # True

# some_data = {'key': 'value', "name": "Jack", "age": 21, "brothers": ("Mark", "Mike")}
#
# ser = json.dumps(some_data)
# print(ser)
# print(type(ser))
# des = json.loads(ser)
# print(des)
# print(type(des))
# print(some_data == des) # False
# =====================================
some_data = {'key': 'value', "name": "Jack", "age": 21, "brothers": ("Mark", "Mike")}
file_name = 'data_2.json'

with open(file_name, "w") as file:
    json.dump(some_data, file)

with open(file_name, "r") as file:
    deser = json.load(file)
    print(deser) # {'key': 'value', 'name': 'Jack', 'age': 21, 'brothers': ['Mark', 'Mike']}


