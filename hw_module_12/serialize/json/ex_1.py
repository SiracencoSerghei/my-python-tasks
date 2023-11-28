import json

d = {'a': 1}
l = [1, 3.3]
t = (3, 4)
s = 'Hello world!'
b = False
st = {1, 2, "Test"}
n = None
int = 5
obj = {"tuple": t, "list": l, 'bool': b, 'str': s, 'none': n, 'int': int}
print(json.dumps(obj))
print(json.dumps(d))
print(json.dumps(l))
print(json.dumps(t))
print(json.dumps(s))
print(json.dumps(b))
# print(json.dumps(st))

with open('storage.json', 'w') as f:
    json.dump(obj, f)
