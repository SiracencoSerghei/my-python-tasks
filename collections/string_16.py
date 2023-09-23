"""Напишите регулярное выражение для функции find_all_links, которая будет в тексте (параметр text) находить все линки и возвращать список полученных из текста совпадений.

В целях упрощения примем, что:

начало гиперссылки может быть http:// или https://
доменное имя — это набор латинских букв, цифр, символов подчеркивания _ и точек .
символы точек . не могут встречаться рядом
Фактически в учебном примере мы будем искать простые url адреса:

https://www.google.com
https://www.facebook.com
https://github.com
Данное регулярное выражение ни в коей мере не претендует на покрытие всех возможных вариантов гиперссылок."""


import re

def find_all_links(text):
    result = []
    iterator = re.finditer(r"https?://(([a-zA-Z0-9_-]+\.)+[a-zA-Z]{2,3})", text)
    for match in iterator:
        result.append(match.group())
    return result

# Приклад використання:
text = "  https://www.google..com   The main search site in the world is https://www.google.com The main social network for people in the world is https://www.facebook.com But programmers have their own social network http://github.com There they share their code. some url to check https://www..facebook.com www.facebook.com"
links = find_all_links(text)
print(links)