# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 22:39:22 2025

@author: Rafik Ncib
"""

def nb_dig(n, d):
    return sum([str(i**2).count(str(d)) for i in range(n+1)])