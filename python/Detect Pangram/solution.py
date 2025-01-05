# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 21:53:49 2025

@author: Rafik Ncib
"""

def is_pangram(st):
    alphabet ="abcderfghijklmnopqrstuvwxyz"
    
    for char in alphabet:
        if(not st.lower().count(char)):
            return False
        
    return True