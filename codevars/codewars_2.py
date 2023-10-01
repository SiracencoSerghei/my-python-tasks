# Given an array of integers.

# Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.

# If the input is an empty array or is null, return an empty array.


def count_positives_sum_negatives(arr):
    count_of_positive_num = 0
    sum_of_negative_num = 0
    
    if not arr or None in arr:
        return []
    
    for num in arr:
        if num > 0:
            count_of_positive_num +=1
        elif num < 0:
            sum_of_negative_num += num
    
    return [count_of_positive_num, sum_of_negative_num]


# def count_positives_sum_negatives(arr):
#   output = []
#   if arr:
#     output.append(sum([1 for x in arr if x > 0]))
#     output.append(sum([x for x in arr if x < 0]))
#   return output


# def count_positives_sum_negatives(arr):
#     pos = sum(1 for x in arr if x > 0)
#     neg = sum(x for x in arr if x < 0)
#     return [pos, neg] if len(arr) else []

numbers = input('enter the numbers: ')
list_of_numbers = list(map(int, numbers.split(" ")))
print(list_of_numbers)

print(count_positives_sum_negatives(list_of_numbers))

