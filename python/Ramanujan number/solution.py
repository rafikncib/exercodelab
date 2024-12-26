# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 17:59:00 2024

@author: Rafik Ncib
"""
import math








def numberRamanujan(max_range=100):
    # Hash table to store n as keys and pairs (a, b) as values
    hash_table = {}
    
    # Compute sums of cubes for all valid (a, b) pairs
    for a in range(1, max_range):
        for b in range(a + 1, max_range):  # Ensure a < b
            n = int(math.pow(a, 3) + math.pow(b, 3))
            if n not in hash_table:
                hash_table[n] = []
            hash_table[n].append((a, b))
    
    # Find the first n with more than one pair
    for n, pairs in hash_table.items():
        if len(pairs) > 1:
            pair1, pair2 = pairs[:2]
            return n, *pair1, *pair2
    
    return "Nothing found"

# Test the function
print(numberRamanujan())
