# List Comprehensions:   [expression for element in iterable if condition]
​
even_nums = []
for x in range(21):
    if x % 2 == 0:
        even_nums.append(x)
print(even_nums)
print([element for element in range(21) if element % 2 == 0 if element % 5 == 0 if element == 20])
​
# if-else
a = ['Парне' if element % 2 == 0 else 'Не парне' for element in range(10)]
print(a)
​
​
# if-elif-else condition
l = [1, 2, 3, 4, 5]
for v in l:
    if v == 1:
        print('yes')
    else:
        if v == 2:
            print('no')
        else:
            print('idle')
​
print(['yes' if v == 1 else 'no' if v == 2 else 'idle' for v in l])