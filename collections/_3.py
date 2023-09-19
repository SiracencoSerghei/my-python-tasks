# def sanitize_phone_number(phone):
#     cleaned_number = phone.replace('(','').replace(')','').replace('-',"").replace('+','').replace(' ','')
#     return cleaned_number
    
# print(sanitize_phone_number("    +38(050)123-32-34"))
# print(sanitize_phone_number("     0503451234"))
# print(sanitize_phone_number("(050)8889900"))

def sanitize_phone_number(phone):
    cleaned_number = phone.strip()
    return cleaned_number
    
print(sanitize_phone_number("    +38(050)123-32-34"))
print(sanitize_phone_number("     0503451234"))
print(sanitize_phone_number("(050)8889900"))
