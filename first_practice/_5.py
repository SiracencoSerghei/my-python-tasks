def has_unique_digits_and_duplicate(number):
    # Перевірка, чи всі цифри унікальні
    digits = str(number)
    if len(set(digits)) == len(digits):
        unique_digits = True
    else:
        unique_digits = False

    # Перевірка, чи є хоча б дві однакові цифри
    duplicate_digits = False
    for digit in digits:
        if digits.count(digit) >= 2:
            duplicate_digits = True
            break

    return unique_digits, duplicate_digits

# Приклади використання функції:
number1 = 123  # Усі різні цифри
number2 = 122  # Є дві однакові цифри
number3 = 456  # Усі різні цифри

result1 = has_unique_digits_and_duplicate(number1)
result2 = has_unique_digits_and_duplicate(number2)
result3 = has_unique_digits_and_duplicate(number3)

print(f"Для числа {number1}: Унікальні цифри: {result1[0]}, Дубльовані цифри: {result1[1]}")
print(f"Для числа {number2}: Унікальні цифри: {result2[0]}, Дубльовані цифри: {result2[1]}")
print(f"Для числа {number3}: Унікальні цифри: {result3[0]}, Дубльовані цифри: {result3[1]}")
