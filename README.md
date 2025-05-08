# 439Exam4_JB
This repository contains code that can be used to read a genomic sequence (a string of characters A,T,G, and C) and return counts of k-mers within the sequence and the frequency of each character following each k-mer. The script should be given an input file containing the genome sequence, the desired k-mer length (or k value), and the name of an output file.



The files within this repo are written for Python3 and utilize the `sys` Python module.

### Files:
- `BIO439_Exam4_JB.py` the script that writes the frequencies of substrings and their following-characters to a given output file
  - `test_get_k_substrings.py` a test script for the "get_k_substrings" function within `BIO439_Exam4_JB.py`
  - `test_count_frequencies.py` a test script for the "count_frequencies" function within `BIO439_Exam4_JB.py`
  - `test_get_following_chars.py` a test script for the "get_following_chars" function within `BIO439_Exam4_JB.py`
  - `test_analyze_genomes.py` a test script for the "analyze_genomes" function within `BIO439_Exam4_JB.py`
  - `test_write_output.py` a test script for the "write_output" function within `BIO439_Exam4_JB.py`
-  `Responses439_JB.txt` a document containing responses to the three prompts given in the assignment guidelines

### How to use:
This script should be ran using Python3.

In the command line, run:

    python BIO439_Exam4_JB.py <input_file> <k-value> <output_file>

The k-value should be an integer.
