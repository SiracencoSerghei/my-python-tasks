from random import randint


def get_random_password():
    
    password = ""
    
    i = 1
    while i <= 8:
        random_num = randint(40, 126)
        ch = chr(random_num)
        password += ch
        i += 1
    return password