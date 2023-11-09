# Dictionary Comprehension:    {<new_key>:<new_value> for <item> in <iterable>}
​
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
temp_C = [30.5, 32.6, 31.8, 33.4, 29.8, 30.2, 29.9]
temperature = {day: temper for day, temper in zip(days, temp_C)}
print(temperature)
​
# Dict Comprehension if-else
numbers = range(10)
new_dict_for = {}
# Add values to `new_dict` using for loop
for n in numbers:
    if n % 2 == 0:
        new_dict_for[n] = n ** 2
print(new_dict_for)
​
​
print({n: n ** 2 for n in range(10) if n % 2 == 0})