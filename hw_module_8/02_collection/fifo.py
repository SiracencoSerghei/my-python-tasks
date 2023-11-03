"""
FIFO (англ. first in, first out - "першим прийшов - першим пішов") - спосіб організації даних або іншими словами черга.
Цей вислів описує принцип технічної обробки черги або обслуговування конфліктних вимог
шляхом упорядкування процесу за принципом: "першим прийшов - першим обслужений".
Той, хто приходить першим, той і обслуговується першим, хто прийде наступним чекає,
поки обслуговування першого не буде закінчено, і так далі.
"""

from collections import deque

MAX_LEN = 5

fifo = deque(maxlen=MAX_LEN)

def push(element):
    fifo.append(element)
def pop():
    return fifo.popleft()

push('Nazar')
push('Olga')
push('Iryna')
push('Ivan')
push('Petro')
print(fifo)
name = pop()
print(name)
print(fifo)
push('Oksana')
print(fifo)
