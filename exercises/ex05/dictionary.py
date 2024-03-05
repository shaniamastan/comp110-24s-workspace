"""EXO5: Dictionary Utility Functions."""

__author__ = "730373934"

def invert(input_dict):
    """Inverts the keys and values of a dictionary."""
    output_dict = {}
    for key, value in input_dict.items():
        if value in output_dict:
            raise KeyError("Duplicate value found in input dictionary so cannot invert.")
        else:
            output_dict[value] = key
    return output_dict


def favorite_color(names_and_colors):
    """Finds the most frequently occurring color."""
    color_count = {}
    for color in names_and_colors.values():
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1
    return max(color_count, key=color_count.get)


def count(values_list):
    """Counts the frequency of each value in a list."""
    result_dict = {}
    for item in values_list:
        if item in result_dict:
            result_dict[item] += 1
        else:
            result_dict[item] = 1
    return result_dict


def alphabetizer(words_list):
    """Categorizes words by their starting letter."""
    result_dict = {}
    for word in words_list:
        letter = word[0].lower()
        if letter not in result_dict:
            result_dict[letter] = [word]
        else:
            result_dict[letter].append(word)
    return result_dict


def update_attendance(attendance_dict, day, student):
    """Updates or adds a student's attendance for a given day."""
    if day in attendance_dict:
        if student not in attendance_dict[day]:
            attendance_dict[day].append(student)
    else:
        attendance_dict[day] = [student]
    return None