"""Your task is to make a function that can take any non-negative integer
 as an argument and return it with its digits in descending order.
  Essentially, rearrange the digits to create the highest possible number.

Examples:
Input: 42145 Output: 54421

Input: 145263 Output: 654321

Input: 123456789 Output: 987654321"""

def descending_order(num):
    if isinstance(num, int) and num >= 0:
        # num_str = str(num)
        # sorted_string = sorted(num_str, reverse=True)
        # sorted_str = ''.join(sorted_string)
        # num = int(sorted_str)
        num = int(''.join(sorted(str(num), reverse=True)))
    return num

print(descending_order(42145))
