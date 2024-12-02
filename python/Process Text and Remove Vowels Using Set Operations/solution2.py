# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 13:30:17 2024

@author: Rafik Ncib
"""

text = 'Programming in python.'
vowels = {'a', 'e', 'i', 'o', 'u'}

text = text.lower()

text = text.replace(' ','')

text = text.replace('.','')

newSet = set(text)

newSet = newSet.difference(vowels)

count = len(newSet)

print("Number of items: ",count)