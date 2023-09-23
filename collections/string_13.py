"""У шостій задачі ми писали функцію is_spam_words, яка визначала, чи є чи ні стоп-слова у тексті повідомлення. Підемо далі та застосуємо функцію sub модуля re для заміни вказаних у списку стоп-слів на деякий шаблон. Наприклад, всі "погані" слова замінюватимемо зірочками. Напишіть функцію replace_spam_words, яка приймає рядок (параметр text), перевіряє його на вміст заборонених слів зі списку (параметр spam_words), та повертає результат рядок, але замість заборонених слів, підставлений шаблон з *, причому довжина шаблону дорівнює довжині забороненого слова. Визначити нечутливість до регістру стоп-слів."""

# # iterable of strings, assume alternation precedence sorting isn't needed
# >>> terms = ['a_42', '(a^b)', '2|3']
# # using 're.escape' and 'join' to construct the pattern
# >>> pat1 = re.compile('|'.join(re.escape(s) for s in terms))
# # using only 'join' to construct the pattern
# >>> pat2 = re.compile('|'.join(terms))

# >>> print(pat1.pattern)
# a_42|\(a\^b\)|2\|3
# >>> print(pat2.pattern)
# a_42|(a^b)|2|3

# ==================================================


import re

def replace_spam_words(text, spam_words):
    # Створюємо регулярний вираз, який відповідає будь-якому слову зі списку spam_words
    pattern = r'\b(?:' + '|'.join(re.escape(word) for word in spam_words) + r')\b'
    print(pattern)
    # Функція, яка буде викликана для кожного збігу
    def replace_word(match):
        return '*' * len(match.group(0))
    
    # Виконуємо заміну в тексті з використанням функції sub
    result = re.sub(pattern, replace_word, text, flags=re.IGNORECASE)
    
    return result
    
# Приклади використання:
print(replace_spam_words("ты хорош но выглядишь как лох", ["лох", "пох"]))  # True
print(replace_spam_words("Молох", ["лох"]))  
print(replace_spam_words("Ты .Лох, но я нет", ["лох"]))  
print(replace_spam_words("сполох ходит далеко", ["лох"]))  