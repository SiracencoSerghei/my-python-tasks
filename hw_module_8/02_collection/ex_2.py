import collections
# Наприклад, є набір температури за перші 15 днів січня.
# Знайти загальну кількість температур, температуру, яка найчастіше зустрічається і т.д.
temps = [0.5, 0.0, -3.5, 0.0, 2.0, 3.5, 0.5, -4.0, -3.5, -0.5, -3.5, -10.5, -14.0, -1.0, -1.0]
tem = collections.Counter(temps)
print(tem)
print(tem.most_common(3))
c = collections.Counter(a=4, b=6, c=1)
print(list(c.elements()))
print(list(c.values()))
print(set(c.elements()))
print(dict(c))

print(tem.most_common()[-1])