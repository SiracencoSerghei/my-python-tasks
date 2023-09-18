'''Напишіть функцію real_len, яка підраховує та повертає довжину рядка без наступних керівних символів: [\n, \f, \r, \t, \v]

Для перевірки правильності роботи функції real_len їй будуть передані наступні рядки:

'Alex\nKdfe23\t\f\v.\r'
'Al\nKdfe23\t\v.\r'  '''

def real_len(text):
    real_text = ''.join(char for char in text if char not in ['\n', '\f', '\r', '\t', '\v'])
    # real_text_list = []
    # for char in text:
    #     if char not in ['\n', '\f', '\r', '\t', '\v']:
    #         real_text_list.append(char)
    # real_text = ''.join(real_text_list)
    return len(real_text)
    
print(real_len('Alex\nKdfe23\t\f\v.\r'))   
print(real_len('Al\nKdfe23\t\v.\r'))   
