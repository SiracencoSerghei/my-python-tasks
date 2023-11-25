# Підрахуйте к-сть кожного символа у строці. Результат повернути у форматі словника

count_letter = {}
for ch in input():
    count_letter[ch] = count_letter.get(ch, 0) + 1
print(count_letter)

from collections import Counter

print(f'{dict(Counter(input()))}')