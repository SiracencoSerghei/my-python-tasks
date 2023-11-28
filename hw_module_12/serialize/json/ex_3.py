# Работа с кирилицею
import json

data = {
    'dev': {
        'name': 'Володимир',
        'test': 'програміст'
    }
}

with open('test.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False)
    # json.dump(data, f)

with open('test.json', 'r', encoding='utf-8') as f:
    restore_data = json.load(f)
    print(restore_data)