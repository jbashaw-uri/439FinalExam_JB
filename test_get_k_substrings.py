import BIO439_Exam4_JB
import pytest

def test_typical_case():
    # Typical test case
    sequence = "ATGCGA"
    k = 2
    expected = ["AT", "TG", "GC", "CG", "GA"]
    assert BIO439_Exam4_JB.get_k_substrings(sequence, k) == expected

def test_k_equals_sequence_length():
    # Testing for strings and substrings of equal length
    # Should return a list with a single substring that is just a copy of the string
    sequence = "ATGC"
    k = 4
    expected = ["ATGC"]
    assert BIO439_Exam4_JB.get_k_substrings(sequence, k) == expected

def test_k_greater_than_sequence_length():
    # Testing for cases where k is larger than the length of the sequence
    # Should return nothing
    sequence = "ATG"
    k = 5
    expected = []
    assert BIO439_Exam4_JB.get_k_substrings(sequence, k) == expected

def test_k_is_zero():
    # Zero-length substrings don't make sense, should return empty
    sequence = "ATGC"
    k = 0
    expected = []
    assert BIO439_Exam4_JB.get_k_substrings(sequence, k) == expected

def test_empty_sequence():
    # No input sequence means no substrings, should return empty
    sequence = ""
    k = 3
    expected = []
    assert BIO439_Exam4_JB.get_k_substrings(sequence, k) == expected