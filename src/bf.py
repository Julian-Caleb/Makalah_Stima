# Brute Force Algorithm
# The Brute Force algorithm searches for a pattern in the text from left to right
# without any special handling, so if there is a mismatch, it only advances
# the index in the text and resets the index in the pattern.
def brute_force_search(pattern, text):
    n = len(text)
    m = len(pattern)
    
    # Iterate through the text
    for i in range(n - m + 1):
        # Check if the pattern matches the substring starting at index i
        match = True
        for j in range(m):
            if text[i + j] != pattern[j]:
                match = False
                break
        
        # If a match is found
        if match:
            return i
    
    # If no match is found
    return -1

