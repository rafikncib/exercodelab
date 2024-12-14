# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 22:41:45 2024

@author: Rafik Ncib
"""

import tkinter as tk
from tkinter import *

# Main Window
window = Tk()
window.title("Double Char")
window.geometry("400x300")
window.configure(bg="#f4f4f4")  # Light gray background

# Function to compute and display the result
def double_char():
    newString = string.get()
    
    labelResult.config(text=''.join([char*2 for char in newString]))

# String Variables
string = StringVar()

# Header Label
header_label = Label(
    window,
    text="Double Char",
    font=("Arial", 16, "bold"),
    bg="#4CAF50",  # Green
    fg="white",
    pady=10,
)
header_label.grid(row=0, column=0, columnspan=2, sticky="nsew")

# First String Input
label_string = Label(
    window, text="Your String:", font=("Arial", 12), bg="#f4f4f4"
)
label_string.grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_string = Entry(
    window, textvariable=string, font=("Arial", 12), bd=2, relief="solid"
)
entry_string.grid(row=1, column=1, padx=10, pady=10, sticky="ew")


# Button to trigger the solution
btnResult = Button(
    window,
    text="Get Result",
    font=("Arial", 12, "bold"),
    bg="#2196F3",  # Blue
    fg="white",
    command=double_char,
    padx=5,
    pady=5,
)
btnResult.grid(row=2, column=0, columnspan=2, pady=10, sticky="ew")

# Label to display the result
labelResult = Label(
    window,
    text="",
    font=("Courier", 14, "bold"),
    bg="#ffffff",  # White background for the result
    fg="#333333",  # Dark gray text
    bd=1,
    relief="solid",
    pady=10,
)
labelResult.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

# Adjust Grid Columns
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=2)

# Run the Main Loop
window.mainloop()