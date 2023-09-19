def is_check_name(fullname, first_name):
    
    # return fullname.startswith(first_name)

    # return fullname[:len(first_name)] == first_name

    return fullname.find(first_name) == 0
    
    
result1 = is_check_name("John Doe", "John") 
result2 = is_check_name("Alice Johnson", "Bob") 
result3 = is_check_name("Sam", "sam")

print(result1)
print(result2)
print(result3)