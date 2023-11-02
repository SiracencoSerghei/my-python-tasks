"""
collections.deque(iterable, [maxlen]) - створює чергу з об'єкта, що ітерується, з максимальною довжиною maxlen.
Черги дуже схожі на списки, за винятком того, що додавати та видаляти елементи можна або праворуч, або ліворуч.

Методи, визначені в deque:
append(x) - додає x до кінця.
appendleft(x) - додає x на початок.
clear() - очищає чергу.
count(x) - кількість елементів, рівних x.
extend(iterable) - додає до кінця всі елементи iterable.
extendleft(iterable) - додає спочатку всі елементи iterable (починаючи з останнього елемента iterable).
pop() - видаляє та повертає останній елемент черги.
popleft() - видаляє та повертає перший елемент черги.
remove(value) - видаляє перше входження value.
reverse() - розгортає чергу.
rotate(n) - послідовно переносить n елементів із кінця на початок (якщо n негативно, то навпаки).
"""
from collections import deque
l = list(range(1, 10))
l_deque = deque(l)
print(l_deque)
right_deque = deque(l, 5)
print(right_deque)
right_deque.append(11)
print(right_deque)
right_deque.appendleft(100)
print(right_deque)
# print(right_deque.count(6))
# print(right_deque.index(100))
right_deque.rotate(2)
print(right_deque)
right_deque.rotate(-2)
print(right_deque)
right_deque.reverse()
print(right_deque)