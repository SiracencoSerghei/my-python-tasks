def prepare_data(data):
    # Проверяем, что список не пустой
    if not data:
        return []

    # Удаляем наименьшее и наибольшее значение
    data.remove(min(data))
    data.remove(max(data))

    # Сортируем список в порядке возрастания
    data.sort()

    return data

# Пример использования функции
data_list = [4, 2, 9, 1, 5, 8, 3, 7, 6]
prepared_data = prepare_data(data_list)
print(prepared_data)