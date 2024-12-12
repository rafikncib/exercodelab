# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 21:34:55 2024

@author: Rafik Ncib
"""

def solution(a, b):
    return a+b+a if len(a)<len(b) else b+a+b


a = input("First string ")
b = input("Second string ")

print(f"the solution of ({a},{b}) is {solution(a,b)}")