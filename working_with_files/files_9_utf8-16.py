"""Есть две строки в разных кодировках - "utf-8" и "utf-16". Нам необходимо понять, равны ли строки между собой.

Реализуйте функцию is_equal_string(utf8_string, utf16_string), которая возвращает True, если строки равны между собой, и False — если нет."""


def is_equal_string(utf8_string, utf16_string):
    
    decoded_utf8_string = utf8_string.decode('utf-8')
    print(decoded_utf8_string)
    decoded_utf16_string = utf16_string.decode('utf-16')
    print(decoded_utf16_string)
    
    
    return decoded_utf8_string == decoded_utf16_string

print(is_equal_string(b'hello Bro', b'\xff\xfeh\x00e\x00l\x00l\x00o\x00 \x00B\x00r\x00o\x00'
))