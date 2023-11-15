# print(dir(str))


# print(str.__doc__)
# print(bool.__doc__)


my_num = 10
other_num = 20

print(my_num.__eq__(other_num))
# print(my_num == other_num)

# print(help(my_num.__add__))

int_num = 5
float_num = 4.5

print(int_num + float_num)

print(int_num.__add__(float_num))

print(float_num.__radd__(int_num))

