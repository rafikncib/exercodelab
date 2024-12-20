# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 18:23:24 2024

@author: Rafik Ncib
"""

def abbrev_name(name):
    
    # Split the name into a list of words using space as a delimiter
    words  = name.split(' ')
    
    # Extract the first character of each word, convert to uppercase, and store in a list
    initials  = [word[0].upper() for word in words ]
    
    # Join the uppercase initials with a period and return the result
    return '.'.join(initials )