"""Вернемся к предыдущей задаче и выполним обратную задачу. Напишите рекурсивную функцию encode для кодирования списка или строки. В качестве аргумента функция принимает список ( например ["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z"]) или строку (например "XXXZZXXYYYZZ"). Функция должна вернуть закодированный список элементов (пример ["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2])."""


def encode(data):
        
    if not data:
        return []
    if isinstance(data, str):
        data = list(data)
        

    value = data[0]
    count = 1

    while len(data) > 1 and data[0] == data[1]:
        data.pop(0)
        count += 1

    return [value, count] + encode(data[1:])




# Приклад використання для кодування
# original_list = ["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z"]
original_list = "XXXZZXXYYYZZ"
encoded_list = encode(original_list)
print(encoded_list)