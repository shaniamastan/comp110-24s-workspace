"""Mutating functions."""


__author__ = "730373934"

def manual_append(numbers: list[int], number: int) -> None:
    """Appends an integer to the end of a list of integers, mutating the original list."""
    numbers.append(number)


def double(numbers: list[int]) -> None:
    """Doubles every element in the list of integers, mutating the original list."""
    index = 0
    while index < len(numbers):
        numbers[index] *= 2
        index += 1