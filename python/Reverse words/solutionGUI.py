# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 19:50:49 2024

@author: Rafik Ncib
"""

# Importing the required library for GUI creation
import tkinter
from tkinter import *

# Initialize the main window
window = Tk()
window.title('Reverse Words')  # Title of the window
window.geometry('400x400')  # Set the window size
window.configure(bg="#f4f4f4")  # Light gray background color

# Declaration of a variable to store user input
string = StringVar()  # StringVar is used to handle the user input in the text field

# Function to reverse words in the input text
def reverse_words():
    """
    Reverses each word in the given text while maintaining the original order of the words.
    """
    # Step 1: Get user input from the entry field
    text = string.get()
    
    # Step 2: Split the input text into words
    words = text.split(' ')  # Splits the text into a list of words by spaces

    # Step 3: Reverse each word and maintain the word order
    reversed_words = [word[::-1] for word in words]  # List comprehension to reverse each word

    # Step 4: Join the reversed words into a single string
    result = ' '.join(reversed_words)  # Combine the reversed words with spaces

    # Step 5: Display the result in the result label
    labelResult.config(text=result)

# Build the widgets for the GUI

# Header Label
header_label = Label(
    window,
    text="Reverse Words",
    font=("Arial", 16, "bold"),  # Font styling
    bg="green",  # Green background
    fg="white",  # White text
    pady=10  # Padding around the text
)
header_label.grid(row=0, column=0, columnspan=2, sticky="nsew")  # Position the header

# Label for the input field
label_string = Label(
    window, 
    text="Your String:", 
    font=("Arial", 12), 
    bg="#f4f4f4"  # Background color matching the window
)
label_string.grid(
    row=1, 
    column=0, 
    padx=10, 
    pady=10, 
    sticky="w"  # Align text to the left
)

# Input field for the user to enter the string
entry_string = Entry(
    window,
    textvariable=string,  # Link the input to the `string` variable
    font=("Arial", 12),  # Font styling
    bd=2,  # Border width
    relief="solid"  # Solid border style
)
entry_string.grid(
    row=1, 
    column=1, 
    padx=10, 
    pady=10, 
    sticky="ew"  # Expand horizontally
)

# Button to trigger the reverse_words function
buttonResult = Button(
    window,
    text="Get Result", 
    font=("Arial", 12, "bold"),  # Font styling
    bg="#2196F3",  # Blue background
    fg="white",  # White text
    command=reverse_words,  # Call the reverse_words function on click
    padx=5, 
    pady=5  # Padding inside the button
)
buttonResult.grid(
    row=2, 
    column=0, 
    columnspan=2,  # Span across two columns
    sticky="ew"  # Expand horizontally
)

# Label to display the result of the reversed string
labelResult = Label(
    window,
    text="",  # Initially empty
    font=("Courier", 14, "bold"),  # Font styling
    bg="#ffffff",  # White background
    fg="#333333",  # Dark gray text color
    bd=1,  # Border width
    relief="solid",  # Solid border style
    pady=10  # Padding around the text
)
labelResult.grid(
    row=3, 
    column=0, 
    columnspan=2,  # Span across two columns
    padx=10, 
    pady=10, 
    sticky="ew"  # Expand horizontally
)

# Adjust column proportions for better layout
window.columnconfigure(0, weight=1)  # First column gets less space
window.columnconfigure(1, weight=2)  # Second column gets more space

# Start the Tkinter event loop
window.mainloop()
