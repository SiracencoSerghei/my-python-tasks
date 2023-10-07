"""Ваша компанія веде блог. Треба реалізувати функцію find_articles для пошуку за статтями цього блогу. Є список articles_dict, в якому міститься опис статей блогу. Кожен елемент цього списку є словником з наступними ключами: прізвища авторів - ключ 'author', назва статті - ключ 'title', рік видання - ключ 'year'.

Реалізуйте функцію find_articles,

Параметр key функції визначає поєднання букв для пошуку. Наприклад, при key="Python" функція шукає, чи є у списку articles_dict статті, у назві чи іменах авторів яких зустрічається це поєднання літер. Якщо такі елементи списку були знайдені, треба повернути новий список зі словників, що містять прізвища авторів, назву та рік видання всіх таких статей.

Другий ключовий параметр функції letter_case визначає, чи треба враховувати під час пошуку регістр літер. За умовчанням він дорівнює False і регістр немає значення тобто пошук в тексті "Python" і "python" це те ж саме. Інакше потрібно шукати повний збіг."""

articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]


# def find_articles(key, letter_case=False):
    
#     results = []
    
#     for article in articles_dict:
#         # тут робимо змінни:
#         author = article['author']
#         title = article['title']
#         year = article['year']
        
#         # print(title.lower().find(key) | author.lower().find(key))
        
#         if letter_case:
#             pair_author = key in author
#             pair_title = key in title
#         else:
#             pair_author = key.lower() in author.lower()
#             pair_title = key.lower() in title.lower()
            
#         if pair_author or pair_title:
#             result = {
#                 'author': author,
#                 'title': title,
#                 'year': year
#             }
#             results.append(result)
            
#     return results
    
        
    
        

    
def find_articles(key, letter_case=False):
    
    results = []
    
    for article in articles_dict:
        # тут робимо змінни:
        author = article['author']
        title = article['title']
        year = article['year']
        
    # author = article['author'], title = article['title'], year = article['year'] in article for article in articles_dict:
        
        # print(title.lower().find(key) | author.lower().find(key))
        
        if letter_case: 
            if title.find(key) != -1 or author.find(key) != -1:
                result = {
                'author': author,
                'title': title,
                'year': year
                }
                results.append(result)
        else: # PythOn pyTHon == True
            if title.lower().find(key.lower()) != -1 or author.lower().find(key.lower()) != -1:
                result = {
                    'author': author,
                    'title': title,
                    'year': year
                    }
                results.append(result)
                    
    return results
    
print(find_articles("ocean", True ) )          
        
        
            

key1 = 'Stark'
key2 = 'ocean'

print(find_articles(key1))
print(find_articles(key2))