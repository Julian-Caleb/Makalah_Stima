# Knuth-Morris-Pratt (KMP) Algorithm
# The KMP algorithm is a method for searching a pattern within a text
# from left to right but more efficiently than brute force by using
# the border array (Border Function) which helps determine the next
# matching position when a mismatch occurs.

# Function to create the border array
# The border array is an array that for each position in the pattern,
# stores the longest prefix which is also a suffix.
# Also known as the border (Longest Prefix Suffix) or failure function.
# Example: for the pattern ['a', 'b', 'a', 'a', 'b', 'a'], its border is
# [0, 0, 1, 1, 2].
def border_function(pattern: str):
    # Initialize variables
    m = len(pattern) - 1
    border = [0] * m
    length = 0
    i = 1

    # The first element of border is always 0
    border[0] = 0

    # Iterate through each element in the pattern, starting from the second element
    while i < m:
        # If there's a match, set border[i] to length 
        # (length of the prefix that matches the suffix up to character index i)
        if pattern[i] == pattern[length]:
            length += 1
            border[i] = length
            i += 1
        # If there's no match, check the length
        else:
            # If there was a previous match, set length to the value of the previous border
            if length != 0:
                length = border[length - 1]
            # If there was no previous match, set it to 0
            else:
                border[i] = 0
                i += 1

    # Return the border array
    return border

# KMP Algorithm
# Function to execute the KMP algorithm using the border array
# created previously to improve efficiency in case of mismatches.
def KMP_search(pattern: str, text: str):
    # Initialize variables
    m = len(pattern)
    n = len(text)
    found = False

    # Create the border array
    border = border_function(pattern)

    # Iterate through indices
    i = 0
    j = 0 

    # While the text is not exhausted,
    while i < n and not found:
        # If characters match, advance both indices
        if pattern[j] == text[i]:
            j += 1
            i += 1

        # If the end of the pattern is reached, the pattern is found in the text, break out of the loop
        if j == m:
            found = True

        # Otherwise, check if the text is not exhausted and if characters do not match.
        elif i < n and pattern[j] != text[i]:
            # If the index for the pattern j is not 0, shift the pattern index according to
            # the value at index j - 1 in the border, allowing partial matches
            if j != 0:
                j = border[j - 1]
            # If j = 0, iterate i
            else:
                i += 1

    if i == n and not found:
        return -1

    return i
