# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 17:59:00 2024

@author: admin
"""
import math







def numberRamanujan(max_range=100):
    hash_table = [
    
    ]
    for a in range(max_range):
        for b in range(max_range):
            if a==b :
                continue
        
            n = math.pow(a,3) + math.pow(a,3)
            hash_table.append({'a':a,'b':b,'n':n})
            
    
    for c in range(max_range):
        for d in range(max_range):
            if c==d :
                continue
            
            n = math.pow(c,3) + math.pow(d,3)
            
            for dic in hash_table:
                if(c != dic['a'] and d != dic['b'] and   n == dic['n']) :
                    return (dic['a'],dic['b'],dic['n'],c ,d , n)
                    break
                
            hash_table.append({'a':a,'b':b,'n':n})

    return "nothing"

print(numberRamanujan())