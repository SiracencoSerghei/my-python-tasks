"""FIFO (англ. first in, first out - "першим прийшов - першим пішов") - спосіб організації даних або іншими словами черга. Цей вислів описує принцип технічної обробки черги чи обслуговування конфліктних вимог шляхом впорядкування процесу за принципом: "першим прийшов - першим обслужений" (ПППО). Той, хто приходить першим, той і обслуговується першим, хто прийде наступним чекає, поки обслуговування першого не буде закінчено, і таке інше.

fifo
За допомогою колекції deque реалізуйте структуру даних FIFO. Створіть змінну fifo, що містить колекцію deque. Обмежте розмір за допомогою константи MAX_LEN. Функція push додає значення element до кінця списку fifo. Функція pop дістає та повертає перше значення зі списку fifo."""

from collections import deque
# Приклад обмеження розміру FIFO до 10 елементів
MAX_LEN = 10
# Створюємо FIFO з обмеженням розміру
fifo = deque(maxlen=MAX_LEN)

def push(element):
    # Додаємо значення в кінець списку
    fifo.append(element)

def pop():
    if fifo:
        # Видаляємо та повертаємо перше значення
        return fifo.popleft()
    else:
        # Повертаємо None, якщо черга пуста
        return None

# Приклад використання:
push(1)
push(2)
push(3)

print(pop())  # Виведе: 1
print(pop())  # Виведе: 2
print(pop())  # Виведе: 3
print(pop())  # Виведе: None (черга пуста)
