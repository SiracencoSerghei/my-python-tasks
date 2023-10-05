"""Всі ви, можливо, стикалися з ребусами "Знайди слово". Вони існують як текстові варіанти, так і як програми для мобільних додатків. Нагадаємо коротко суть ребуса. У великому квадраті з набором букв необхідно знайти слово по горизонталі та інколи по вертикалі. Реалізуйте функцію solve_riddle(riddle, word_length, start_letter, reverse=False) для знаходження слова, що шукається в рядку ребуса.

Параметри функції:

riddle - рядок із зашифрованим словом.
word_length – довжина зашифрованого слова.
start_letter - літера, з якої починається слово (мається на увазі, що до початку слова літера не зустрічається в рядку).
reverse - вказує, у якому порядку записане слово. За замовчуванням — в прямому. Для значення True слово зашифроване у зворотньому порядку, наприклад, у рядку 'mi1rewopret' зашифроване слово 'power'.
Функція повинна повертати перше знайдене слово. Якщо слово не знайдене, повернути пустий рядок."""


def solve_riddle(riddle, word_length, start_letter, reverse=False):
   # Перевертаємо рядок, якщо reverse=True
    if reverse:
        riddle = riddle[::-1]
    first_index_word = riddle.find(start_letter)
    last_index_word = first_index_word + word_length
    return riddle[first_index_word:last_index_word]

# Приклад використання:
riddle = "mi1rewopret"
word_length = 5
start_letter = "p"
reverse = True
result = solve_riddle(riddle, word_length, start_letter, reverse)
print(result)  # Виведе: "power"