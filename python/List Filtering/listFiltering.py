# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 14:51:51 2024

@author: Rafik Ncib
"""

def filter_list(l):
    
    'return a new list with the strings filtered out'
    return [element for element in l if(not isinstance(element,str))]