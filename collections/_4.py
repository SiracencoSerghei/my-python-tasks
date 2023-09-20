def is_check_name(fullname, first_name):

    # return fullname.startswith(first_name)

    # return fullname[:len(first_name)] == first_name

    return fullname.find(first_name) == 0


result_1 = is_check_name("John Doe", "John")
result_2 = is_check_name("Alice Johnson", "Bob")
result_3 = is_check_name("Sam", "sam")

print(result_1)
print(result_2)
print(result_3)
