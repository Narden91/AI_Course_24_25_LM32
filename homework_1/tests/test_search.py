import pytest
from src.homework.search import binary_search_iterative, binary_search_recursive


@pytest.fixture
def sorted_list():
    return [1, 3, 5, 7, 9, 11, 13, 15]


def test_binary_search_iterative_found(sorted_list):
    assert binary_search_iterative(sorted_list, 7) == 3


def test_binary_search_iterative_not_found(sorted_list):
    assert binary_search_iterative(sorted_list, 8) == -1


def test_binary_search_iterative_empty():
    assert binary_search_iterative([], 5) == -1


def test_binary_search_recursive_found(sorted_list):
    assert binary_search_recursive(sorted_list, 7, 0, len(sorted_list) - 1) == 3


def test_binary_search_recursive_not_found(sorted_list):
    assert binary_search_recursive(sorted_list, 8, 0, len(sorted_list) - 1) == -1


def test_binary_search_recursive_empty():
    assert binary_search_recursive([], 5, 0, -1) == -1
