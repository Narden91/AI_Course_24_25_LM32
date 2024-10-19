import pytest
from src.homework.text_ops import count_words, find_longest_word, format_sentences


@pytest.fixture
def sample_text():
    return "Python is an amazing programming language! It is easy to learn."


def test_count_words(sample_text):
    result = count_words(sample_text)
    assert result['python'] == 1
    assert result['is'] == 2
    assert len(result) == 7


def test_count_words_empty():
    assert count_words("") == {}


def test_find_longest_word(sample_text):
    assert find_longest_word(sample_text) == "programming"


def test_find_longest_word_empty():
    assert find_longest_word("") == ""


def test_format_sentences(sample_text):
    result = format_sentences(sample_text)
    assert len(result) == 2
    assert result[0].startswith("Python")
    assert result[1].startswith("It")
