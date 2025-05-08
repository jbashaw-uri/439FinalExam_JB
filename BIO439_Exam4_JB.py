import sys   #importing sys package for file fetching

def get_k_substrings(s, k): 
    """
    Excract all substrings of length k from the input sequence "s"
    
    Parameters:
    s : str
        The input genome string of characters A,T,C, or G
    k : int
        The desired length of each substring
        
    Returns:
    list: A list of substrings of length k
    """
    
    #extracts all substrings of length k from the string
    if k <= 0 or len(s) < k:   #including part here to return a blank list if k is set to 0
        print ("Invalid k value. k cannot be negative, 0, or a number greater than the total number of characters in the sequence.")
        sys.exit()
    else:
        return [s[i:i + k] for i in range(len(s) - k + 1)]

def count_frequencies(items):
    """
    Count how many times each substring appears in a list.

    Parameters:
    items : list
        A list of items to count.

    Returns:
    dict: A dictionary with substring counts.
    """
    
    freq = {}          #empty list
    for item in items:      #counts each substring and adds value to list
        freq[item] = freq.get(item, 0) + 1
    return freq

def get_following_chars(s, k):
    """
    For each k-length substring in the sequence, count the frequency of the character
    that immediately follows it.

    Parameters:
    s : str
        The input genome sequence.
    k : int
        The length of the substrings.

    Returns:
    dict: A nested dictionary where keys are substrings and values are dictionaries
          of following character frequencies.
    """
    
    followers = {}
    for i in range(len(s) - k):  
        substring = s[i:i + k]   #extract each substring of length k
        next_char = s[i + k]     #get the character immediately after each substring

        if substring not in followers: 
            followers[substring] = {}  #initializes the nested directory if the substring isn't already present in the list
        followers[substring][next_char] = followers[substring].get(next_char, 0) + 1  #adds count of each following character to each nested substring directory
    return followers

def analyze_genome(s, k):
    """
    Uses previously defined functions to perform substring counts and counts of each following character.

    Parameters:
    s : str 
        The genome sequence.
    k : int 
        The length of substrings to analyze.

    Returns:
    tuple: A tuple of two dictionaries:
           - substring_counts: frequency of each substring
           - followers: characters that follow each substring and their counts
    """
    
    substrings = get_k_substrings(s, k)               #get all substrings of length k
    substring_counts = count_frequencies(substrings)  #count the frequency of each substring
    followers = get_following_chars(s, k)             #get the frequency of each character following each substring
    return substring_counts, followers

def write_output(output_file, substring_counts, followers):
    """
    Write the substring counts and followers to the specified output file.
    
    Parameters:
    output_file : str
        Path to the output file
    substring_counts : dict
        Counts of each substring
    followers : dict
        Frequencies of characters following each substring
    """
    with open(output_file, 'w') as f:  #open the specified output file in write mode
        f.write("Substring counts:\n")   #creates header for substring counts part of file
        for kmer, count in substring_counts.items(): #writes each substring's frequency to the file
            f.write(f"{kmer}: {count}\n")  #leaves a blank line between sections

        f.write("\nFollowers:\n")     #creates header for following character frequencies part of file
        for kmer, next_chars in followers.items(): #writes the frequency of each substring's following characters to the file
            follower_str = ', '.join(f"{char}: {cnt}" for char, cnt in next_chars.items()) #formats list of followers as a comma separated string
            f.write(f"{kmer}: {follower_str}\n") #leaves a blank line between sections

def main():
    """
    Main function that reads the input file and substring size from the command line then:
        Validates the inputs on the command line
        Reads the provided genome sequence
        Counts substrings and characters following substrings
        Writes the results to the output file
    """
    
    if len(sys.argv) != 4:                             #returns error if input on command line is not exactly 3 arguments (input file, k-mer length, and output file)
        print("Usage: python BIO439_Exam4_JB.py <input_file> <k> <output_file>")
        sys.exit(1)

        #extract the three arguments from the command line
    input_file = sys.argv[1]
    k = int(sys.argv[2])
    output_file = sys.argv[3]

    with open(input_file, 'r') as f:
        sequence = f.read().replace('\n', '').strip().upper()  #removes newlines and spaces from the sequence while also converting entirely to uppercase in the case of input errors
        
    if len(sequence) <= k:                          #returns error if k is too large for the script to work on the given sequence
        print("Error: Substring length k is too large for the given sequence.")
        sys.exit(1)

    substring_counts, followers = analyze_genome(sequence, k)  #performs counts of substrings and following characters
    write_output(output_file, substring_counts, followers)   #writes outputs of those counts to the output file
    print(f"Results written to {output_file}")              #informs the user that the results were successfully written to the file

if __name__ == "__main__":  #call the main function if the script is run directly
    main()