def is_spam_words(text, spam_words, space_around=False):
    text = text.lower()
    
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    
    text = ''.join(char for char in text if char not in punctuation)
    print(f'space_around: {space_around}')
    print(f'text: {text}')
    
    words = text.split()
    
    for word in spam_words:
        if space_around:
            if word in words:
                return True
            
        else:
            for w in words:
                if word in w:
                    return True
    
    return False

# Приклади використання:
print(is_spam_words("ты хорош но выглядишь как лох", ["лох"]))  # True
print(is_spam_words("Молох", ["лох"], True))  # False
print(is_spam_words("Ты лох.", ["лох"]))  # True
print(is_spam_words("сполох ходит далеко", ["лох"], True))  # True