"""EXO4 - List Utility Functions."""

__author__ = "730373934"


# all Function
def all(numbers: list[int], match: int) -> bool:
    """Checks if every number in the list is the same as the specified number."""
    if len(numbers) == 0:
        return False
    for number in numbers:
        if number != match:
            return False
    return True


# max Function
def max(numbers: list[int]) -> int:
    """Finds and returns the largest number in the list or errors if empty."""
    if len(numbers) == 0:
        raise ValueError("max() arg is an empty List")
    maximum = numbers[0]
    for number in numbers[1:]:
        if number > maximum:
            maximum = number
    return maximum


# is_equal Function
def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Determines if two lists have the same elements in the same order."""
    if len(list1) != len(list2):
        return False
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
    return True


# extend Function
def extend(list1: list[int], list2: list[int]) -> None:
    """Adds all elements from the second list to the end of the first."""
    for number in list2:
        list1.append(number)