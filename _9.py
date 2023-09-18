def is_valid_pin_codes(pin_codes):
    # Перевірка на пустий список
    if not pin_codes:
        return False
    
    # Перевірка довжини пін-кодів та наявності лише цифр
    for code in pin_codes:
        if len(code) != 4 and not code.isdigit():
            return False
    
    # Перевірка на наявність дублікатів
    if len(pin_codes) != len(set(pin_codes)):
        return False
    
    return True