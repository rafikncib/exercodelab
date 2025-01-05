# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 21:56:47 2025

@author: Rafik Ncib
"""

def divisors(n):
    ls= [i  for i in range(1,n//2+1) if n%i==0]
    return len(ls)+1