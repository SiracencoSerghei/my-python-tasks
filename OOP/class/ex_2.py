"""
Розбираємо різницю між: звичайним методом, @classmethod и @staticmethod
"""


class Compare:
    a = 5

    def doubler(self, x):  # self = test (тобто назва екземпляра класу)
        print('Mul on 2')
        return x * 2

    @staticmethod
    def triples(x):
        print('Mul on 3')
        return x * 3

    @classmethod
    def quad(cls, x):  # cls = Compare (клас)
        print('Mul on 4')
        return x * 4

test = Compare()
print('Екземпляри класу')
print(test.doubler(5))
print(test.triples(5))
print(test.quad(5))
print('Виклик через клас')
# print(Compare.doubler(6))
print(Compare.triples(6))
print(Compare.quad(6))
