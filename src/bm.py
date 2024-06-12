# Boyer-Moore Algorithm
# The Boyer-Moore algorithm is a string matching algorithm that searches a 
# text from left to right, but matching starts from the right end of the pattern 
# and moves to the left. The Boyer-Moore algorithm utilizes two techniques: 
# the looking-glass technique and the character-jump technique, which will be 
# discussed in the program. The Boyer-Moore algorithm also uses the Last 
# Occurrence Function which returns an array containing the last index of 
# each character (ASCII) appearing in the pattern.

# Function to return an array containing the last index
# of each ASCII character appearing in the pattern.
# The array will have a length of 256, each corresponding to an ASCII character,
# and if the character does not appear in the pattern, it will be filled with -1.
def last_occurrence_function(pattern):
    # 256 ASCII characters
    last = [-1] * 256
    # Fill the array with the last index of each character's occurrence
    for i in range(len(pattern)):
        last[ord(pattern[i])] = i
    return last

# BMSearch Algorithm
# Function to execute the Boyer-Moore algorithm on a text
# by calling the last_occurrence_function to get the
# array of the last index for each ASCII character (-1 if not present)
# in the pattern, then applying the looking-glass technique
# and the character-jump technique.
@staticmethod
def BM_search(pattern, text):
    # Instantiate variables
    last = last_occurrence_function(pattern)
    m = len(pattern)
    n = len(text)
    found = False
    
    # Iterate over the index, moving from left to right in the text
    # Check from right to left in the pattern.
    i = m - 1
    j = m - 1

    # Perform the iteration
    while i < n and not found:
        # If there is a match
        if pattern[j] == text[i]:
            # If it is the first character
            if j == 0:
                found = True
            # If not, apply the looking-glass technique
            # Looking-glass technique: searching P in T by moving backward
            # from the end.
            else:
                i -= 1
                j -= 1
        # If there is a mismatch, apply the character-jump technique
        # Character-jump technique: If there is a mismatch, with T[i] = x,
        # and P[j] != x, handle one of the following 3 cases:
        # 1. If P has x to the left of j, shift P to the right to align with the last index of x.
        # 2. If P has x to the right of j, shift P to the right by 1 character to T[i+1].
        # 3. If x is not in P, shift P so that P[0] = T[i+1].
        else:
            lo = last[ord(text[i])]
            i = i + m - min(j, 1 + lo)
            j = m - 1

    # If no match is found
    if i > n - 1 and not found:
        return -1
    
    return i
