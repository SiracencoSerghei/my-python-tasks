from copy import deepcopy, copy


class Expenses:
    def __init__(self):
        self.data = {}
        self.places = []

    def spent(self, place, value):
        self.data[str(place)] = value
        self.places.append(place)

    def __copy__(self):
        copy_obj = Expenses()
        copy_obj.data = self.data
        copy_obj.places = self.places
        return copy_obj

    def __deepcopy__(self, memo):
        copy_obj = Expenses()
        memo[id(copy_obj)] = copy_obj
        copy_obj.data = deepcopy(self.data)
        copy_obj.places = deepcopy(self.places)
        return copy_obj

# =======================================

e = Expenses()
e.spent('hotel', 100)
e.spent('taxi', 10)
print(e.places)             # ['hotel', 'taxi']

e_copy = copy(e)
print(e_copy is e)          # False
e_copy.spent('bar', 30)
print(e.places)             # ['hotel', 'taxi', 'bar']

e_deep_copy = deepcopy(e)
print(e_deep_copy is e)     # False
e_deep_copy.spent(
    'airport',
    300
)
print(e.places)             # ['hotel', 'taxi', 'bar']
print(e_deep_copy.places)   # ['hotel', 'taxi', 'bar', 'airport']

"""Using the __copy__ and __deepcopy__ methods, you can control how 
exactly a copy of your object is created. The __deepcopy__ method must
take one argument - a dictionary in which all objects that are copied 
are written. This is necessary to avoid endless recursion if some object 
is common to several being copied. In this case, the deep copy algorithm
can go into an infinite loop, alternately copying objects with references 
to each other. The memo dictionary stores object ids as keys and the 
objects themselves as values. When we redefine how copying should occur,
we may not use memo if we know for sure that recursion will not occur."""
