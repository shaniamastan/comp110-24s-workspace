"""EXO5: Dictionary Utility Functions."""

__author__ = "730373934"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of a dictionary."""
    output_dict = {}
    for key, value in input_dict.items():
        if value in output_dict:
            raise KeyError("Duplicate value found in input dictionary so cannot invert.")
        else:
            output_dict[value] = key
    return output_dict


def favorite_color(names_and_colors: dict[str, str]) -> str:
    """Finds the most frequently occurring color."""
    color_count: dict[str, int] = {}
    for color in names_and_colors.values():
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1

    most_frequent_color = None
    highest_count = 0
    for color in names_and_colors.values():
        if color_count[color] > highest_count or most_frequent_color is None:
            most_frequent_color = color
            highest_count = color_count[color]
    return most_frequent_color if most_frequent_color is not None else ""


def count(values_list: list[str]) -> dict[str, int]:
    """Counts the frequency of each value in a list."""
    result_dict: dict[str, int] = {}
    for item in values_list:
        if item in result_dict:
            result_dict[item] += 1
        else:
            result_dict[item] = 1
    return result_dict


def alphabetizer(words_list: list[str]) -> dict[str, list[str]]:
    """Categorizes words by their starting letter."""
    result_dict: dict[str, list[str]] = {}
    for word in words_list:
        letter = word[0].lower()
        if letter not in result_dict:
            result_dict[letter] = [word]
        else:
            result_dict[letter].append(word)
    return result_dict


def update_attendance(attendance_dict: dict[str, list[str]], day: str, student: str) -> None:
    """Updates or adds a student's attendance for a given day."""
    if day in attendance_dict:
        if student not in attendance_dict[day]:
            attendance_dict[day].append(student)
    else:
        attendance_dict[day] = [student]