# Під капотом функції copy, deepcopy роблять нічого більше,
# ніж викликають методи __copy__, __deepcopy__.
from collections import UserList
from copy import copy, deepcopy

class CopyList(UserList):
    def __init__(self, *args):
        super().__init__()
        self.data = list(args)

    def __copy__(self):
        n = CopyList()
        n.data = self.data
        return n

    def __deepcopy__(self, memodict={}):
        n = CopyList()
        memodict[id(self)] = n  # {"140640986278160": [1, 2, 3, 4]}
        print(memodict)
        for element in self.data:
            n.append(deepcopy(element, memodict))
        return n


data = CopyList([1, 2, 3, 4])
data_copy = copy(data)
data_deep = deepcopy(data)

print(id(data), data)
print(id(data_copy), data_copy)
print(id(data_deep), data_deep)

print(id(data[0]), data[0])
print(id(data_copy[0]), data_copy[0])
print(id(data_deep[0]), data_deep[0])