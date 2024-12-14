# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 22:18:53 2024

@author: Rafik Ncib
"""

def smash(words):
    sentence = ""
    for i in range(len(words)):
        sentence += words[i].strip()  # Remove any extra spaces
        if i < len(words) - 1:
            sentence += " "  # Add a space after each word except the last
    return sentence
