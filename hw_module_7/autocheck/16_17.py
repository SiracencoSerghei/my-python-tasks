"""Разберем простую технику кодирования и декодирования на основе серий. Например, у нас есть список с повторяющимися наблюдениями какой-то величины, она может принимать значения X, Y или Z. Значения появляются в произвольном порядке и храним мы их в списке ["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z"] или строке "XXXZZXXYYYZZ".

За счет чего мы можем уменьшить объем хранимой информации? Сжатие можно достичь заменой группы повторяющихся значений на однократное значение и счетчик повторов: ["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]

Напишите рекурсивную функцию decode для декодирования списка, закодированного этим способом. В качестве аргумента функция принимает закодированный список. Функция должна вернуть расшифрованный список элементов."""


def decode(data):
    if not data:
        return []
    value = data[0]
    count = data[1]
    
    # result = [value] * count
    # result.extend(decode(data[2:]))
    # return result
    
    return [value] * count + decode(data[2:])

# Приклад використання для розкодування
encoded_list = ["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]
decoded_list = decode(encoded_list)
print(decoded_list)