import BIO439_Exam4_JB
import pytest

def test_count_frequencies_typical():
    # Test for a typical case with single character substrings
    items = ["A", "G", "A", "C", "G", "A"]
    expected = {"A": 3, "G": 2, "C": 1}
    assert BIO439_Exam4_JB.count_frequencies(items) == expected

def test_count_frequencies_typical_multiple():
    # Like previous test, but testing for multiple character substrings
    items = ["AGC", "GTA", "AGC", "CTC", "GTG", "AGA", "CTC", "GAG", "GTA", "AGC"]
    expected = {"AGC": 3, "GTA": 2, "CTC": 2, "GTG": 1, "AGA": 1, "GAG": 1}
    assert BIO439_Exam4_JB.count_frequencies(items) == expected
    
def test_count_frequencies_empty():
    # Tests that counting an empty list returns an empty dictionary
    assert BIO439_Exam4_JB.count_frequencies([]) == {}

def test_count_frequencies_all_unique():
    # Tests that each item gets a count of 1 if every item is unique
    assert BIO439_Exam4_JB.count_frequencies(["X", "Y", "Z"]) == {"X": 1, "Y": 1, "Z": 1}
