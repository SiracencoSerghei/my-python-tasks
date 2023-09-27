points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}

def calculate_distance(coordinates):
    
    total_distance = 0
    # range(len(coordinates) - 1) тому що останній координат не мае последующего...
    for i in range(len(coordinates) - 1):
        if len(coordinates) <= 1:
            return 0
    
    #     point1 = coordinates[i]
    #     point2 = coordinates[i + 1]
        
    #     # Перевірка на порядок координат
    #     if (point1, point2) in points:
    #         total_distance += points[(point1, point2)]
    #     else:
    #         # Якщо координати не відповідають порядку в словнику, обмінюємо їх місцями
    #         total_distance += points[(point2, point1)]
        
    # return total_distance
    
    total_distance = sum(points.get((coordinates[i], coordinates[i + 1]), points.get((coordinates[i + 1], coordinates[i]), 0)) for i in range(len(coordinates) - 1))
    return total_distance

# Приклад виклику функції зі списком координат
coordinates = [0, 1, 3, 2, 0, 2]
result = calculate_distance(coordinates)
print(result)  # Виведе відстань