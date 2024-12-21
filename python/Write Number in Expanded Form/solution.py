# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 18:49:44 2024

@author: Rafik Ncib
"""

def expanded_form(num):
    # Convert the number into a string to easily access individual digits
    ch = str(num)
    
    # Use a list comprehension to generate the expanded form for each non-zero digit
    # Iterate through the string, index by index
    # For each digit, multiply it by 10 raised to the power of its position from the right
    # Example: For 70304, '7' -> '70000', '3' -> '300', '4' -> '4'
    ls = [ch[i] + "0" * (len(ch) - i - 1) for i in range(len(ch)) if ch[i] != "0"]
    
    # Join the list of expanded values with " + " to form the final string
    return " + ".join(ls)
