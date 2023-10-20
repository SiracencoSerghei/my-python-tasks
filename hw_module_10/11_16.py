"""Створіть клас NumberString, успадкуйте його від класу UserString, визначте для нього метод number_count(self), який буде рахувати кількість цифр у рядку."""

from collections import UserString
# import re

class NumberString(UserString):
    # def number_count(self):
    #     pattern = r'\d'
    #     count = len(re.findall(pattern, self.data))
    #     return count
    def number_count(self):
        count = sum(1 for char in self.data if char.isdigit())
        return count

# Example usage:
text = NumberString("Hello 123 World 456")
count = text.number_count()
print(f'The string has {count} digits.')