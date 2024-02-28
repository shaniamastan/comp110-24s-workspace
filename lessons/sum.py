"""Summing the elements of a list using different loops."""

__author__ = "730373934"


# Part 1: w_sum
def w_sum(vals: list[float]) -> float:
    """Calculates the sum of a list of floats using a while loop."""
    number_of_vals = len(vals) - 1
    index = 0

    sum_of_vals = 0.0

    while index <= number_of_vals:

        sum_of_vals += vals[index]
        index += 1

    return sum_of_vals


# Part 2: f_sum
def f_sum(vals: list[float]) -> float:
    """Calculates the sum of a list of floats using a for loop."""
    sum_of_vals = 0.0

    for val in vals:
        sum_of_vals += val

    return sum_of_vals


# Part 3:
def f_range_sum(vals: list[float]) -> float:
    """Calculates the sum of a list of floats by iterating over their indices with a for loop."""
    sum_of_vals = 0.0

    for index in range(0, len(vals)):  # Added missing whitespace after ','
        sum_of_vals += vals[index]

    return sum_of_vals
