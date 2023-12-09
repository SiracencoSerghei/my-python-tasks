import sys

def square_generator(n):
    for i in range(1, n+ 1):
        yield i
        # yield i*i
        # yield i*i*i
        # yield i*i*i*i
        
for i in square_generator(3):
    print(i)
    
print(square_generator(5))
print(list(square_generator(5)))

print(sys.getsizeof(square_generator(2225)))
print(sys.getsizeof(list(square_generator(2225))))
print(sys.getsizeof(square_generator))

hello = square_generator(5)
print(next(hello))
print(next(hello))
print(next(hello))


def boys():
    yield "Phillip"
    yield 'Steve'
    
    
def girls():
    yield "Sarah"
    yield "Emily"   
    
def names(also_boys=True):
    yield from girls()
    if also_boys:
        yield from boys()
        

# Example 1: Using a loop
hello = names()
print(hello)
while True:
    try:
        print(next(hello))
    except StopIteration:
        break

# Example 2: Using list()
print(list(names()))

