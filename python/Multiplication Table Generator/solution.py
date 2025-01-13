# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 20:17:04 2025

@author: Rafik Ncib
"""



while(True):
    number =  input("Enter a number ")
    try:
        number = int(number)
        break
    except:
        print("error")

print(number)

for i in range(11):
    product = number * i
    print(f'{number} x {i} = {product}')