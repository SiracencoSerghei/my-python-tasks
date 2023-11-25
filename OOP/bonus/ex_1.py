# Вам задано рядок символів s. Виведіть суму ASCII значень всіх символів
s = input()
x = 0
for item in s:
    x += ord(item)
print(x)


print(sum(map(ord, input())))