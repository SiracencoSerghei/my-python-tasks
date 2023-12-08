
my_list = ['a', 'b', 'c', 'd', 'e']

print(dict(enumerate(my_list, start=1)))

my_dict = {el:pos for pos, el in enumerate(my_list, start=1)}
print(my_dict) 
