import yaml
# pip install PyYAML

users = [
    {'name': 'Микола', 'age': 32, 'gender': 'male'},
    {'name': 'Марія', 'age': 44, 'gender': 'female'},
    {'name': 'Ігор', 'age': 55, 'gender': 'male'},
]
serialize = yaml.dump(users)
result = yaml.load(serialize, Loader=yaml.FullLoader)
print(result)

with open('test.yaml', 'w', encoding='utf-8') as f:
    yaml.dump({"users": users}, f, allow_unicode=True)
