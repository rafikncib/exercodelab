# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 13:29:21 2024

@author: Rafik Ncib
"""

text = 'Programming in python.'
vowels = {'a', 'e', 'i', 'o', 'u'}

text = text.lower()

text = text.replace(' ','')

text = text.replace('.','')

newSet = {i for i in text}

newSet.difference_update(vowels)

count = len(newSet)
 
print("Number of items: ",count)

