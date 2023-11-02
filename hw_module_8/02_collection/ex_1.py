"""
Іменовані кортежі
Клас collections.namedtuple дозволяє створити тип даних, що поводиться як кортеж з можливістю привласнити кожному
елементу ім'я, яким надалі можна отримати доступ
"""

import collections

Cat = collections.namedtuple('Cat', ['nickname', 'age', 'owner'])
cat_object = Cat('Boris', 3, 'Andriy')
print(cat_object.nickname)
print(cat_object.age)
print(cat_object.owner)
print(type(cat_object))
tup = ('nickname', 'age', 'owner')
print(tup)
print(type(tup))