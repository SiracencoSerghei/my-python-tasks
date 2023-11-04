

my_list = [1, 2, 3]
copy_list = my_list
copy_list.append(4)
print(my_list)  # [1, 2, 3, 4]


my_list = [1, 2, 3]
copy_list = my_list[:]
copy_list.append(4)
print(my_list)  # [1, 2, 3]

d = {1: 'a'}
d_copy = {**d}
d_copy[2] = 'b'
print(d)        # {1: 'a'}


"""But you can't do that with custom types. To solve this problem,
 Python has a copy mechanism - these are functions
  from the copy package."""

import copy


my_list = [1, 2, {1: 'a'}]
copy_list = copy.copy(my_list)
copy_list.append(4)
print(my_list)      # [1, 2, {1: 'a'}]
print(copy_list)    # [1, 2, {1: 'a'}, 4]

copy_list[2][2] = 'b'
#  can't do deep copy because in both lists is link to dict {1: 'a'}:
print(my_list)    # [1, 2, {1: 'a', 2: 'b'}]
