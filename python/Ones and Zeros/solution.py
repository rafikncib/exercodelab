# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 22:55:22 2024

@author: Rafik Ncib
"""

import math

def binary_array_to_number(arr):
    # Get the length of the array to calculate the power of 2 for each binary digit
    lengthArr = len(arr)
    # Iterate over the array, calculate the weighted sum of binary digits
    return sum([arr[num] * math.pow(2, lengthArr - num - 1) for num in range(lengthArr)])
