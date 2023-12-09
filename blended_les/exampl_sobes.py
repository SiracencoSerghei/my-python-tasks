# fizzbuzz
# linear search
# binary search
# regular expression
# OOP
# recursion
# dynamic programming


def binary_search(lst, start, end, searched_item):
    if start <= end:
        middle = (end + start) // 2 
        if lst[middle] == searched_item:
            return middle
        if searched_item > lst[middle]:
            return binary_search(lst, middle + 1, end, searched_item)
        else:
            return binary_search(lst, start, middle - 1, searched_item)
    return -1




# print(binary_search(lst2, 0, len(lst2) - 1, 3))

def binarySearch(array, target):
    return binarySearchHelper(array, target, 0, len(array)-1)

def binarySearchHelper(array, target, left, right):
    if left > right:
        return -1        
    
    midle =(left + right) // 2
    potentionalMatch = array[midle]
    if target == potentionalMatch:
        return midle
    elif target < potentionalMatch:
        return binarySearchHelper(array, target, left, midle - 1)
    else:
        target > potentionalMatch
        return binarySearchHelper(array, target, midle + 1, right)
        
lst2 = [2, 4, 5, 6,7, 8, 10, 12 ]
print(binarySearch(lst2, 12))

