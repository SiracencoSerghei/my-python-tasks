from decimal import Decimal, getcontext, ROUND_HALF_EVEN, ROUND_HALF_UP

# Встановлення точності для обчислень з Decimal
getcontext().prec = 10  # Встановлення точності на 10 десяткових розрядів

# Приклад використання Decimal для точних арифметичних операцій
decimal_result = Decimal('10.5') / Decimal('3')
print(decimal_result)


# f = 0.2 + 0.1 +0.3 - 0.5
# print(f)
# result = Decimal("0.2") + Decimal('0.1') + Decimal('0.3') - Decimal('0.5')
# print(result)
# n = Decimal("1") / Decimal("3")
# print(n)
# print(type(n))

getcontext().prec = 4
# n = Decimal("1") / Decimal("3")
# print(n)
# n = Decimal("11") / Decimal("3")
# print(n)
# n = Decimal("110") / Decimal("3")
# print(n)
# n = Decimal("110000") / Decimal("3")
# print(float(n))
# print(110000/3)
# ================
# num = Decimal('1.45')
# print(num.quantize(Decimal('1.0'), rounding=ROUND_HALF_EVEN)) # by default
# print(num.quantize(Decimal('1.0'), rounding=ROUND_HALF_UP)) # by human
print(Decimal('3.14159').quantize(Decimal('1.000')))

# ======================
print(0.1 + 0.2)
print(Decimal(1.1) + Decimal(0.2))
print(Decimal('1.1') + Decimal('0.2'))
