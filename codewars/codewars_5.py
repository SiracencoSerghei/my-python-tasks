"""Build a function that returns an array of integers from n to 1 where n>0.

Example : n=5 --> [5,4,3,2,1]"""
def reverse_range_list(n:int)->list:
    # return list(reversed(range(1, n+1)))
    return list(range(n, 0, -1))
 
print(reverse_range_list(5))
 