"""EXO4 - List Utility Functions."""

__author__ = "730373934"

# all Function
def all(numbers: list[int], match: int) -> bool:
    if len(numbers) == 0:
        return False  # Returns False if the list is empty
    for number in numbers:
        if number != match:
            return False  # Short-circuit if any number doesn't match
    return True  # All numbers matched

# max Function
def max(numbers: list[int]) -> int:
    if len(numbers) == 0:
        raise ValueError("max() arg is an empty List")
    maximum = numbers[0]
    for number in numbers[1:]:
        if number > maximum:
            maximum = number
    return maximum

# is_equal Function
def is_equal(list1: list[int], list2: list[int]) -> bool:
    if len(list1) != len(list2):
        return False  # Lists of different lengths cannot be equal
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False  # Found elements that are not equal
    return True  # All elements matched

# extend Function
def extend(list1: list[int], list2: list[int]) -> None:
    for number in list2:
        list1.append(number)  # Mutate list1 by appending all elements of list2


