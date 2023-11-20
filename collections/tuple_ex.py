screen_res = (1920, 1080)

print(screen_res)
print(type(screen_res))
print(isinstance(screen_res, tuple))
print(id(screen_res))

print(screen_res.count(1080))
print(screen_res.index(1920))

screen_res_list = list(screen_res)
screen_res_list[0] = 1444
print(screen_res_list)

screen_res = tuple(screen_res_list)
print(screen_res)
print(id(screen_res))

screen_res = (1920, 1080)
screen_info = (True, 'Samsung', 150)

screen_data = screen_res + screen_info
print(screen_data)
print(screen_res)
print(screen_info)

print(screen_data[0])
print(screen_data[-1])
print(len(screen_data))

post_ids = (151, 245)
post_ids_list = list(post_ids)
post_ids_list.append(351)
post_ids_tuple = tuple(post_ids_list)
print(post_ids)
print(post_ids_tuple)
post_ids = post_ids_tuple
print(post_ids)
