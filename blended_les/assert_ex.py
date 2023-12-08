import random

def return_even_number():
    return 4


assert return_even_number() % 2 == 0

def create_a_string_of_length_four():
    result = ''
    for i in range(4):
        result += chr(random.randint(1, 126))
    return result
        
print(create_a_string_of_length_four())

assert len(create_a_string_of_length_four()) == 4
assert isinstance(create_a_string_of_length_four(), str)

def return_a_random_number_between_zero_and_one():
    return random.random()*2

print(return_a_random_number_between_zero_and_one())

assert 0 <= return_a_random_number_between_zero_and_one() <= 1