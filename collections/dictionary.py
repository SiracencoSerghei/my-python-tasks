# # users = [{'user_id': 134, 'user_name': 'Alice'},
# #          {'user_id': 831, 'user_name': 'Bob'},
# #          {'user_id': 898, 'user_name': 'Sergio'}]
# #
# # print("len: ", len(users))
# # for user in users:
# #     print("User_ID: ", user['user_id'])
# #     print("User_Name: ", user['user_name'])
# #     if user['user_name'] == 'Sergio':
# #         user['user_name'] = 'Pietro'
# #         print("User_Name: ", user['user_name'])
# # print(users)
#
# from collections import UserDict
#
#
# class MyDict(UserDict):
#     def __add__(self, other):
#         self.data.update(other)
#         return self
#
#     def __sub__(self, other):
#         for key in other:
#             if key in self.data:
#                 self.data.pop(key)
#         return self
#
#
# d1 = MyDict({1: 'a', 2: 'b', 3: 'D'})
# d2 = MyDict({3: 'c', 4: 'd'})
#
# d3 = d1 + d2
# print(d3)  # {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
#
# d4 = d3 - {10: 'ww', 2: 'b'}
# print(d4)  # {1: 'a', 3: 'c', 4: 'd'}


my_bike = {
    'brand': 'Ducati',
    'color': 'red'
}
my_string = 'abcd'
my_list = ['a', 10, 'b', 20]
# print((dict(my_string))) # Error
# print(dict(my_list))  # Error
my_list_2 = [['a', 10], ['b', 20]]
my_list_of_tuples = [('a', 10), ('b', 20)]
print(dict(my_list_2))  # {'a': 10, 'b': 20}
print(dict(my_list_of_tuples))  # {'a': 10, 'b': 20}
