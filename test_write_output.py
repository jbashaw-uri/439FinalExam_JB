import BIO439_Exam4_JB
import pytest

def test_write_output_file(tmp_path):
    # Testing to ensure that everything is written correctly to the output file
    substring_counts = {"AT": 2, "TG": 1}
    followers = {
        "AT": {"G": 2},
        "TG": {"C": 1}
    }

    # Using pytest's "tmp_path" option to create a temporary output file for the test
    output_file = tmp_path / "output.txt"

    # Writing the results to the temporary output file
    BIO439_Exam4_JB.write_output(str(output_file), substring_counts, followers)

    # Reading the output file and checking to make sure the expected lines are present
    with open(output_file) as f:
        content = f.read()

    # Making sure the expected substring counts and follower counts are present in the output
    assert "AT: 2" in content
    assert "TG: 1" in content
    assert "AT: G: 2" in content
    assert "TG: C: 1" in content