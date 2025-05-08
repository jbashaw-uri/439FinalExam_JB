import BIO439_Exam4_JB
import pytest

def test_analyze_genome_typical():
    # Tests the combined result of k-mer counting and follower tracking on a simple genome
    s = "ATGCG"
    k = 2
    substrings_expected = {"AT": 1, "TG": 1, "GC": 1, "CG": 1}
    followers_expected = {
        "AT": {"G": 1},
        "TG": {"C": 1},
        "GC": {"G": 1}
    }
    substrings, followers = BIO439_Exam4_JB.analyze_genome(s, k)
    assert substrings == substrings_expected
    assert followers == followers_expected
    
def test_analyze_genome_complex():
    # Does the same as above, but with a more complex genome to check for snags 
                   #(I manually went through the genome and counted substrings + followers for this one)
    s = "CGTACGTACGCATATGCACGTCGTCATCAGTACGTCAGCTACGT"
    k = 2
    substrings_expected = {"CG": 7, "GT": 7, "TA": 5, "AC": 5, "GC": 3, "CA": 5, "AT": 3, "TG": 1, "TC": 4, "AG": 2, "CT": 1}
    followers_expected = {
        "CG": {"T": 6, "C": 1},
        "GT": {"A": 3, "C": 3},
        "TA": {"C": 4, "T": 1},
        "AC": {"G": 5},
        "GC": {"A": 2, "T": 1},
        "CA": {"T": 2, "C": 1, "G": 2},
        "AT": {"A": 1, "G": 1, "C": 1},
        "TG": {"C": 1},
        "TC": {"G": 1, "A": 3},
        "AG": {"T": 1, "C": 1},
        "CT": {"A": 1}
    }