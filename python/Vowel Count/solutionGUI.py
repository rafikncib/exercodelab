# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 22:46:01 2024

@author: Rafik Ncib
"""

import tkinter as tk
from tkinter import *

# Initialize the main window
window = Tk()
window.geometry("400x400")
window.title("Vowel Counter")

# Styling configurations
title_font = ("Helvetica", 16, "bold")
label_font = ("Arial", 12)
button_font = ("Arial", 10, "bold")

# Title Label
title_label = Label(window, text="Vowel Counter", font=title_font, fg="blue")
title_label.pack(pady=15)

# Function to count vowels in the input string
def count_vowels():
    sentence = number.get() # Convert to lowercase for case-insensitivity
    vowels = "aeiou"
    
    vowel_count = sum(sentence.count(vowel) for vowel in vowels.lower() )  # Sum counts of each vowel
    label_result.config(text=f"'{sentence}' has {vowel_count} vowel(s).", fg="green")
    number.set("")  # Clear the entry

# Function to clear the input and output
def clear():
    number.set("")
    label_result.config(text="")

# Entry widget to input the sentence
number = StringVar()
entry = Entry(window, textvariable=number, font=label_font, width=30)
entry.pack(pady=10)

# Button to count vowels
button_count = Button(window, text="Count Vowels", font=button_font, bg="lightgreen", command=count_vowels)
button_count.pack(pady=5)

# Button to clear the input/output
button_clear = Button(window, text="Clear", font=button_font, bg="lightcoral", command=clear)
button_clear.pack(pady=5)

# Label to display the result
label_result = Label(window, text="", font=label_font, wraplength=300, justify="center")
label_result.pack(pady=20)

# Run the application
window.mainloop()
