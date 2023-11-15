# long_str = 'It\'s a great day today'
# very_long_str = "This is very" \
#                 " very long," \
#                 " very long string"
# most_long_str = ("This is very, very very, very very, very very, very very, "
#                  "very very, very very, very very, very very, very very, "
#                  "very very, very very, very very, very very, very "
#                  "very, very long string")
#
# print(long_str)
# print(very_long_str)
# print(most_long_str)
# print(type(long_str))
#
# print(very_long_str.count('long'))  # 2
# print((very_long_str.count('is')))  # 2
# print(long_str[:-1])
# print(long_str[::-1])
#
# print(long_str.find('great'))
# print(long_str.split(" "))
#
# print(dir(long_str))

name = "Sergio"
hobby = "running"
time = 8

# info = name + ' likes ' + hobby + ' at ' + str(time) + " o'clock"
# info = "{} likes {} at {} o'clock".format(name, hobby, time)
info = f"{name} likes {hobby} at {time} o'clock"
info2 = "%s likes %s at %s o'clock" % (name, hobby, time)

print(info)
print(info2)
