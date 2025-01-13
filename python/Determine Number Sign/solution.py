# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 20:47:24 2025

@author: Rafik Ncib
"""

# Write a program to determine if a number is positive, negative, or zero.

while(True):
    user_input = input("Enter a number: ")
    try:
        # Try to convert input to an integer
        number = int(user_input)
        break
    except ValueError:
        try:
            # If integer conversion fails, try to convert input to a float
            number = float(user_input)
            break
        except ValueError:
            print("Invalid input. Please enter a valid number (integer, float).")
                    

if number == 0:
    print(f"{number} is zero")
elif number > 0:
    print(f"{number} is positive")
else:
    print(f"{number} is negative")