import pickle

d = {"data": 12345}
with open('lesson.bin', 'wb') as file:
    pickle.dump(d, file)  # запис серіалізованого обєкту у файл. Файл буде бінарним

d_bytes = pickle.dumps(d)  # повертає серіалізований обєкт. Його можна використовувати
print(d_bytes)

with open('lesson.bin', 'rb') as file:
    d_load = pickle.load(file)  # зчитуємо і десералізуємо обєкт
print(d_load)

d_loads = pickle.loads(d_bytes)  # повертає серіалізований обєкт. Його можна використовувати
print(d_loads)


# dump i load - використовуємо при роботі з файлами
# dumps i loads - використовуємо при передачі по мережі
