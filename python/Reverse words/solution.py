# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 15:04:00 2024

@author: Rafik Ncib
"""

def reverse_words(text):
    """
    Reverses each word in the given text while maintaining the original order of the words.
    
    Args:
    text (str): A string containing words separated by spaces.

    Returns:
    str: A string with each word reversed but the word order preserved.
    """
    
    # Step 1: Split the input text into a list of words
    words = text.split(' ')  # Splits the string by spaces into individual words

    # Step 2: Reverse each word in the list using list comprehension
    reversed_words = [word[::-1] for word in words]  # Reverses each word in the list

    # Step 3: Join the reversed words back into a single string, separated by spaces
    result = ' '.join(reversed_words)  # Joins the reversed words with spaces
    
    return result  # Return the final reversed string
