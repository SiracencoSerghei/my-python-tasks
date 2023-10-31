import  collections

Cat = collections.namedtuple('Cat', ['nickname', 'age', 'owner'])
cat = Cat('Boris', 3, "Andrii")
print(cat.nickname)
print(cat.age)
print(cat.owner)
print(type(cat))

tup = ('nickname', 'age', 'owner')
print(tup)
print(type(tup))

temp = [0.5, 0.7, 9.3, 12.2, 0.5, 0.7, 0.5]
tem = collections.Counter(temp)
print(tem)
print(tem.most_common(3))
c = collections.Counter(a=4, b=6, c=0)
print(list(c.elements()))
print(list(c.values()))
print(set(c.elements()))
print(dict(c))
print(tem.most_common())
print(tem.most_common()[-1])

data = collections.defaultdict(list)
data[0].append(1)
data[0].append(2)
data[0].append(3)
data[1].append(10)
data[1].append(11)
data[2].append(110)
print(data)

data_dict = collections.defaultdict(dict)
data_dict['a'] = 4 # defaultdict(<class 'dict'>, {'a': 4})
print(data_dict)

l = list(range(1, 10))
print(l)
l = collections.deque(l)
print(l)
left_l = collections.deque(l, 5)
print(left_l)

left_l.appendleft(110)
print(left_l)
print(left_l.count(5))




