# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 10:38:45 2025

@author: Rafik Ncib
"""

string = "abc"
result = []
long = len(string)

result = ['']
for char in string:
    new_result = []
    for seq in result:
        for k in range(len(seq)+1):
            new_char = seq[:k]+char+seq[k:]
            new_result.append(new_char)
    result=new_result   
    
print(result)


from itertools import permutations

for x in permutations(['a', 'b', 'c']):
    print(''.join(x))