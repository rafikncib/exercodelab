# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 00:06:53 2025

@author: Rafik Ncib
"""

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
   

    new_list = []
    
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if(i+j+k != n):
                    new_list.append([i,j,k])            
    
    print(new_list)