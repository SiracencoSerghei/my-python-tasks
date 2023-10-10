"""Створіть функцію decimal_average(number_list, signs_count), яка обчислюватиме середнє арифметичне типу Decimal з кількістю значущих цифр signs_count. Параметр number_list — список чисел

Увага
Не забувайте приводити всі числа у списку до типу `decimal`

Приклад:

виклик функції decimal_average([3, 5, 77, 23, 0.57], 6) поверне 21.714
виклик функції decimal_average([31, 55, 177, 2300, 1.57], 9) поверне 512.91400"""

from decimal import Decimal, getcontext


def decimal_average(number_list, signs_count):
    context = getcontext()
    context.prec = signs_count
    
    def sum_numbers(numbers):
        if len(numbers) == 0:
            return Decimal(0)
        return Decimal(numbers[0]) + sum_numbers(numbers[1:])

    sum_num_list = sum_numbers(number_list)
    print(f'sum: {sum_num_list}')
    
    
   
    average = Decimal(sum_num_list) / Decimal((len(number_list)))
    
    print(average)
    return average

   
    
decimal_average([3, 5, 77, 23, 0.57], 6)
decimal_average([31, 55, 177, 2300, 1.57], 9)


# виклик функції decimal_average([3, 5, 77, 23, 0.57], 6) поверне 21.714
# виклик функції decimal_average([31, 55, 177, 2300, 1.57], 9) поверне 512.91400
