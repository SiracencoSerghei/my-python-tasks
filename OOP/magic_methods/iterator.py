#
# for i in range(10):
#     print(i, end=", ")
#
# class Iterator:
#     def __init__(self):
#         self.start = 0
#     def __next__(self):
#         self.start += 1
#         if self.start == 100:
#             raise StopIteration
#         return self.start
# class MyIterable:
#
#     def __iter__(self):
#         return Iterator()
#
#
# my_iter = MyIterable()
# for i in my_iter:
#     print(i, end=", ")
#

# ===========================
# class Iterator:
#     def __init__(self):
#         self.start = -1
#     def __next__(self):
#         self.start += 1
#         if self.start == 100:
#             raise StopIteration
#         return self.start
#
#     def __iter__(self):
#         return self
#
#
# my_iter = Iterator()
# for i in my_iter:
#     print(i, end=", ")
# ====================================

# class RangeIterator:
#     def __init__(self, start, stop, step=1):
#         self.start = start
#         self.stop = stop
#         self.step = step
#
#     def __next__(self):
#         if self.start >= self.stop:
#             raise StopIteration
#         result = self.start
#         self.start += self.step
#         return result
#
#     def __iter__(self):
#         return self
#
# my_iter = RangeIterator(10, 55, 5)
# for i in my_iter:
#     print(i, end=", ")
# ==============================

# class ListIterator:
#     def __init__(self, values):
#         self.values = values
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index >= len(self.values):
#             raise StopIteration
#         value = self.values[self.index]
#         self.index += 1
#         return value
#
# # Example usage:
# my_list = [1, 2, 3, 4, 5]
# my_iterator = ListIterator(my_list)
#
# for value in my_iterator:
#     print(value)
# ===================================

class DictIterator:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.keys = list(dictionary.keys())
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.keys):
            raise StopIteration
        key = self.keys[self.index]
        value = self.dictionary[key]
        self.index += 1
        return key, value

# Example usage:
my_dict = {"a": 1, "b": 2, "c": 3}
my_iterator = DictIterator(my_dict)
for key, value in my_iterator:
    print(f"{key}: {value}")
