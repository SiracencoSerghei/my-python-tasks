import collections

t = 'This is the text'
d = {}
for c in t:
    if c in d:
        d[c] += 1
    else:
        d[c] = 1

a = collections.Counter()
for c in t:
    a[c] += 1
print(d)
print(a)
b = collections.Counter(t)
print(b)
print(list(b.elements()))
print(b.most_common())

f = {}
for word in t.split(' '):
    if len(word) in f:
        f[len(word)].append(word)
    else:
        f[len(word)] = [word]
print(f)
g = collections.defaultdict(list)
for word in t.split(' '):
    g[len(word)].append(word)
print(g)
v = collections.deque(b.elements())
print(v)
v.rotate(5)
print(v)
v.appendleft("1, 2")
print(v)

