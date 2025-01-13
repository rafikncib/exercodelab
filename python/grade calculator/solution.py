# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 21:10:43 2025

@author: Rafik Ncib
"""

# Create a simple grade calculator (e.g., A, B, C).
def grade(number):
    if(number < 60):
        return "F"
    
    if(number < 70):
        return "D"
    
    if number < 80:
        return "C"
    
    if number < 90:
        return "B"
    
    return "A"

while(True):
    user_input = input("Enter your score: ")
    try:
        number = int(user_input)
        break
    except ValueError:
        try:
            number = float(user_input)
            break
        except ValueError:
            print("Invalid input. Please enter a valid number (integer, float).")


print(f"Grade for score {number} is {grade(number)}")




    