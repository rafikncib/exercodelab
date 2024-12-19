# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 20:45:24 2024

@author: Rafik Ncib
"""

def min_max(lst):
  
    # Sort the list
    lst.sort()
    
    # Return the smallest and largest numbers
    return [lst[0], lst[-1]]