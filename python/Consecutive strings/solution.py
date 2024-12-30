# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 23:17:29 2024

@author: Rafik Ncib
"""

def longest_consec(strarr, k):
    # Check if k is invalid: either non-positive or greater than the length of the array.
    # If so, return an empty string since it's not possible to form a valid sequence.
    if k <= 0 or k > len(strarr):  
        return ''
    
    # Initialize a variable to store the longest concatenated string.
    first_longest = ""
    
    # Iterate through the array up to the point where k consecutive strings can still be selected.
    for i in range(len(strarr) - k + 1):  
        # Compute the concatenated string for the current k elements starting at index i.
        current_concatenation = ''.join(strarr[i:i + k])  
        
        # Compare the length of the current concatenated string with the longest found so far.
        # If the current one is longer, update the `first_longest` variable.
        if len(first_longest) < len(current_concatenation):  
            first_longest = current_concatenation
    
    # Return the longest concatenated string found during the iteration.
    return first_longest
