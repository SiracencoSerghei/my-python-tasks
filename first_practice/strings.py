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


"""Move the first letter of each word to the 
end of it, then add "ay" to the end of the 
word. Leave punctuation marks untouched.


"""

# def pig_it(text):
#     punctuation =".\"',;:/"
#     words = text.split()
#     for i in range(len(words)):
#         if not words[i].isalpha():
#             continue
#         if words[i].endswith(tuple(punctuation)):
#             words[i] = words[i][1:-1] + words[i][0] + 'ay' +words[i][-1]
#         else:
#             words[i] = words[i][1:] +words[i][0] + 'ay'
#     return " ".join(words)

from string import punctuation
def pig_it(text):
    words = text.split(' ')
    return ' '.join(
        [
            '{}{}ay'.format(
                word[1:],
                word[0]
            ) if word not in punctuation else word for word in words
        ]
    )
    