# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 13:52:55 2024

@author: Rafik Ncib
"""

def get_count(sentence):
    # String contains all vowels exepts y
    vowelString="aeiou"
    
    # initialize number of vowels in the given string (sentence)
    nbreVowelsString=0
    
    # loop in the vowelString
    # and each time count the number of time this vowel in the sentence string
    
    for vowel in vowelString:
        nbreVowelsString += sentence.count(vowel) 
    
    return nbreVowelsString
    
    
    