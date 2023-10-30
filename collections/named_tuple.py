import collections

Book = collections.namedtuple("Book", ["title", "author", "number_of_pages", "ISBN"])
py = Book("The Art of Computer Programming", "Donald E; Knuth", 3168, "978-0321751041")
print(py.author)  # Donald E; Knuth
print(py[1])     # Donald E; Knuth
print(Book._fields)   # ('title', 'author', 'number_of_pages', 'ISBN')
