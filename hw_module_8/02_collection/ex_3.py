"""
defaultdict
collections.defaultdict нічим не відрізняється від звичайного словника за винятком того,
що за замовчуванням завжди викликається функція, що повертає значення
"""
from collections import defaultdict
# {key_1: [], key_2: [], key_3: [] ...}
data = defaultdict(list)
data[0].append(1)
data[0].append(2)
data[0].append(3)
data[1].append(10)
data[1].append(11)
data[2].append(110)
print(data)

data_dict = defaultdict(dict)
data_dict[0] = 4
data_dict[0] = 5
data_dict[1] = 6
print(data_dict)
