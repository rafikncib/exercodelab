# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 17:03:21 2024

@author: Rafik Ncib
"""

def likes(names):
    if names == []:
        return "no one likes this"
    elif len(names) == 1:
        return f"{names[0]} likes this"
    elif len(names) == 2:
        return f"{names[0]} and {names[1]} like this"
    elif len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {len(names) - 2} others like this"
