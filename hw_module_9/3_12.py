""" 
концепцію замикання може добре пояснити приклад кешування значень функції. 
Підсумкове завдання модуля 3 було — рекурсивне обчислення чисел Фібоначчі.
Ряд Фібоначчі - це послідовність чисел виду: 0, 1, 1, 2, 3, 5, 8, ..., 
де кожне наступне число послідовності виходить додаванням двох попередніх членів ряду.
У загальному вигляді для обчислення n-го члена ряду Фібоначчі потрібно 
вирахувати вираз: Fn = Fn-1 + Fn-2.
Це завдання можна вирішити рекурсивно, викликаючи функцію, що обчислює 
числа послідовності доти, доки виклик не сягне членів ряду менше n = 1, де послідовність задана.
Створіть функцію caching_fibonacci(), яка матиме кеш із попередньо 
обчисленими значеннями чисел Фібоначі. Усередині вона містить функцію 
fibonacci(n), яка безпосередньо і обчислюватиме саме число Фібоначчі. 
Функція caching_fibonacci() повертає функцію fibonacci
Якщо число Фібоначчі зберігається у словнику cache, то функція fibonacci 
повертає число з кеша. Якщо його немає у кеші, то ми обчислюємо число і 
поміщаємо його в кеш, і повертаємо з функції fibonacci.
"""

# def caching_fibonacci():
#     """caching_fibonacci"""
#     # Створімо словник для зберігання результатів обчислення чисел Фібоначчі
#     cache = {}

#     def fibonacci(n):
#         # Перевірка, чи число Фібоначчі знаходиться в кеші
#         if n in cache:
#             return cache[n]
#         # Якщо число Фібоначчі не знайдено в кеші, обчислюємо його
#         if n == 0:
#             result = 0
#         elif n == 1:
#             result = 1
#         else:
#             result = fibonacci(n - 1) + fibonacci(n - 2)
#         # Зберігаємо результат обчислення в кеші
#         cache[n] = result
        
#         print(cache)
#         return result
#     return fibonacci

# # Створення функції для обчислення чисел Фібоначчі з кешуванням
# n=5
# calculate_fib = caching_fibonacci()

# # Приклад використання:
# N = 10
# # result1 = calculate_fib(N)
# # print(f"Fibonacci({N}) = {result1}")
# result2 = calculate_fib(n)
# print(f"Fibonacci() = {result2}")
# # End-of-file
def cache_results(func):
    """Декоратор для кешування результатів"""
    cache = {}  # Словник для зберігання результатів

    def wrapper(n):
        if n in cache:
            return cache[n]
        result = func(n)
        cache[n] = result
        return result

    return wrapper

@cache_results
def fibonacci(n):
    """Обчислення чисел Фібоначчі"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = 5
result = fibonacci(n)
print(f"Fibonacci({n}) = {result}")