import BIO439_Exam4_JB
import pytest

def test_get_following_chars_typical():
    # Tests follower counts for typical 2 unit k-mers
    s = "ATGCG"
    k = 2
    expected = {
        "AT": {"G": 1},
        "TG": {"C": 1},
        "GC": {"G": 1}
    }
    assert BIO439_Exam4_JB.get_following_chars(s, k) == expected

def test_get_following_chars_no_followers():
    # Tests that if a substring is at the end of the string, it won't have any following characters and will return nothing
    assert BIO439_Exam4_JB.get_following_chars("ATG", 3) == {}

def test_get_following_chars_overlap():
    # Tests repeated overlapping substrings and correct follower counting
    s = "AAAA"
    k = 2
    expected = {
        "AA": {"A": 2}
    }
    assert BIO439_Exam4_JB.get_following_chars(s, k) == expected

def test_get_following_chars_empty_string():
    # Tests that an empty sequence returns no followers
    assert BIO439_Exam4_JB.get_following_chars("", 2) == {}