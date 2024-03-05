"""Splitting a dictionary into two lists."""

__author__ = "730373934"


def get_keys(input_dict: dict[str, int]) -> list[str]:
    """Making a list of keys."""
    keys_list = list()
    for key in input_dict:
        keys_list.append(key)
    return keys_list


def get_values(input_dict2: dict[str, int]) -> list[int]:
    """Making a list of values."""
    values_list = list()
    for value in input_dict2:
        values_list.append(input_dict2[value])
    return values_list