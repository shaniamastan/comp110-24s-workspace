"""EXO6: Dictionary Unit Tests."""

__author__ = "730373934"

import pytest
from exercises.ex05.dictionary import invert, count, favorite_color, alphabetizer, update_attendance

# invert function tests


def test_invert_normal_case():
    """Test normal case of inverting a dictionary."""
    input_dict = {'a': '1', 'b': '2', 'c': '3'}
    expected_output = {'1': 'a', '2': 'b', '3': 'c'}
    assert invert(input_dict) == expected_output


def test_invert_empty_dict():
    """Test inverting an empty dictionary."""
    assert invert({}) == {}


def test_invert_key_error():
    """Test inverting a dictionary with duplicate values raises KeyError."""
    with pytest.raises(KeyError):
        invert({'a': '1', 'b': '1'})


# count function tests
def test_count_multiple_occurrences():
    """Test counting with multiple occurrences of elements."""
    assert count(['a', 'b', 'a', 'c', 'b', 'a']) == {'a': 3, 'b': 2, 'c': 1}


def test_count_single_element():
    """Test counting with a single element in the list."""
    assert count(['a']) == {'a': 1}


def test_count_empty_list():
    """Test counting with an empty list."""
    assert count([]) == {}


# favorite color function tests
def test_favorite_color_common_case():
    """Test finding the most frequent color in a typical case."""
    names_and_colors = {'Alice': 'blue', 'Bob': 'red', 'Charlie': 'blue', 'David': 'green'}
    assert favorite_color(names_and_colors) == 'blue'


def test_favorite_color_tie():
    """Test finding the most frequent color when there is a tie."""
    names_and_colors = {'Alice': 'blue', 'Bob': 'red', 'Charlie': 'blue', 'David': 'red'}
    assert favorite_color(names_and_colors) in ['blue', 'red']


def test_favorite_color_empty_dict():
    """Test finding the most frequent color in an empty dictionary."""
    assert favorite_color({}) == ""


# alphabetizer function tests
def test_alphabetizer_normal_case():
    """Test alphabetizing a list of words."""
    words_list = ['apple', 'banana', 'apricot', 'cherry']
    expected_output = {'a': ['apple', 'apricot'], 'b': ['banana'], 'c': ['cherry']}
    assert alphabetizer(words_list) == expected_output


def test_alphabetizer_single_word():
    """Test alphabetizing a single word."""
    assert alphabetizer(['apple']) == {'a': ['apple']}


def test_alphabetizer_empty_list():
    """Test alphabetizing an empty list."""
    assert alphabetizer([]) == {}


# update attendance function tests
def test_update_attendance_existing_day():
    """Test updating attendance for an existing day."""
    attendance_dict = {'Monday': ['Alice', 'Bob']}
    update_attendance(attendance_dict, 'Monday', 'Charlie')
    assert attendance_dict == {'Monday': ['Alice', 'Bob', 'Charlie']}


def test_update_attendance_new_day():
    """Test updating attendance for a new day."""
    attendance_dict = {'Monday': ['Alice', 'Bob']}
    update_attendance(attendance_dict, 'Tuesday', 'Charlie')
    assert attendance_dict == {'Monday': ['Alice', 'Bob'], 'Tuesday': ['Charlie']}


def test_update_attendance_existing_student():
    """Test updating attendance where the student is already present."""
    attendance_dict = {'Monday': ['Alice']}
    update_attendance(attendance_dict, 'Monday', 'Alice')
    assert attendance_dict == {'Monday': ['Alice']}
