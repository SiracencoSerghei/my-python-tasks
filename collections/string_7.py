CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

TRANS = {}
    
    

# Створюйте словник TRANS поза функцією translate:

def create_trans_dict():
    for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        TRANS[ord(c)] = l
        TRANS[ord(c.upper())] = l.upper()

# Визов функції для створення словника TRANS
create_trans_dict()

def translate(name):
    name = name.translate(TRANS)
    return name  

# Приклад виконання:
print(translate("Дмитро Короб"))  # Dmitro Korob
print(translate("Олекса Івасюк"))  # Oleksa Ivasyuk