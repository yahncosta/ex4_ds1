import pytest

from unique_element import find_unique_element


def test_example_case():
    assert find_unique_element([1, 2, 3, 4, 3, 1, 2]) == 4


def test_single_item():
    assert find_unique_element([7]) == 7


def test_negative_numbers():
    assert find_unique_element([-1, -2, -1, -3, -2]) == -3


def test_even_length_input():
    with pytest.raises(RuntimeError):
        find_unique_element([1, 1, 2, 3])


def test_no_unique_element():
    with pytest.raises(RuntimeError):
        find_unique_element([1, 1, 2, 2, 3, 3, 4])


def test_multiple_unique_elements():
    with pytest.raises(RuntimeError):
        find_unique_element([1, 2, 3])


def test_element_occurs_three_times():
    with pytest.raises(RuntimeError):
        find_unique_element([1, 1, 1, 2, 2])