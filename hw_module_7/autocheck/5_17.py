"""Дуже часто люди у своїх повідомленнях не ставлять великі літери, особливо це стало масовим явищем в еру мобільних. пристроїв. Розробіть функцію capital_text, яка прийматиме на вхід рядок з текстом і повертатиме рядок з відновленими великими літерами.

Функція повинна:

зробити великою першу літеру в рядку, попри прогалини
зробити великою першу літеру після точки, попри прогалини
зробити великою першу літеру після знака оклику, попри прогалини
зробити великою першу літеру після знака питання, попри прогалини"""


def capital_text(text):
    # Перевірка на порожній рядок
    if not text:
        return text
    # Зробимо великою першу літеру в рядку а останні маленькімі...
    text = text.lower().capitalize()
    is_next_word_capitalize = False
    for ch in text:
        print(ch)
        
    
    
    
# Приклад використання:
text = "hello. how are you! i'm fine, thank you?"
capitalized_text = capital_text(text)
print(capitalized_text)