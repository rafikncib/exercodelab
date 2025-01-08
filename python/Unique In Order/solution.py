# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 22:27:27 2025

@author: Rafik Ncib
"""

def unique_in_order(sequence):
    if(not sequence):
        return []
    ls = [x for x in sequence]
    
    ls1 = [ls[0]]
    for i in range(0,len(ls)-1):
        if(ls[i]!=ls[i+1]):
            ls1.append(ls[i+1])
            
    return (ls1)
    
    
    