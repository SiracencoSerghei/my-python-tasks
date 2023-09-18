# def is_valid_password(password):
#     if len(password) != 8:
#         return False
    
#     if not any(char.isupper() for char in password):
#         return False
        
#     if not any(char.islower() for char in password):
#         return False
    
#     if not any(char.isdigit() for char in password):
#         return False
    
#     return True

# print(is_valid_password('3WTc1oFv'))


def is_valid_password(password):
    # Check if the password length is 8 characters
    if len(password) != 8:
        return False

    contains_upper = False
    contains_lower = False
    contains_digit = False

    for char in password:
        if char.isupper():
            contains_upper = True
        if char.isdigit():
            contains_digit = True
        if char.islower():
            contains_lower = True

    # Check if the password contains at least one uppercase letter and one digit
    if contains_upper and contains_digit and contains_lower:
        return True

    return False