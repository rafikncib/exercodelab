def remove_smallest(numbers):
    ls = list(numbers)
    if(not ls):
        return []
    smallestNumber=min(numbers)
    smallestNumberIndex = ls.index(smallestNumber)
    ls.pop(smallestNumberIndex)
    return ls