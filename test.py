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
        
        # print(title.lower().find(key) | author.lower().find(key))
        
        if letter_case:
            if title.find(key) != -1 or author.find(key) != -1:
                result = {
                'author': author,
                'title': title,
                'year': year
                }
                results.append(result)
        else:
            if title.lower().find(key.lower()) != -1 or author.lower().find(key.lower()) != -1:
                result = {
                    'author': author,
                    'title': title,
                    'year': year
                    }
                results.append(result)
                    
    return results
    
print(find_articles("ocean", True ) )          
        
        
            