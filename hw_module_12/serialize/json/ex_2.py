import json

with open('storage.json', 'r') as f:
    store = json.load(f)
print(store)