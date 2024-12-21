# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 18:52:30 2024

@author: Rafik Ncib
"""

# Importing the required library for GUI creation
import tkinter
from tkinter import *

# Initialize the main window
window = Tk()
window.title('Write Number in Expanded Form')  # Title of the window
window.geometry('500x400')  # Set the window size
window.configure(bg="#f4f4f4")  # Light gray background color

# Declaration of a variable to store user input
string = StringVar()  # StringVar is used to handle the user input in the text field

# Function to generate the expanded form of a number
def expanded_form():
    """
    Converts the given number into its expanded form.
    Example: 70304 --> '70000 + 300 + 4'
    """
    # Get user input from the entry field
    ch = string.get().strip()  # Remove leading/trailing whitespace

    # Validation: Check if the input is a valid integer
    if not ch.isdecimal():
        labelResult.config(
            text="Error: Only non-negative integers are allowed.",
            fg="red"  # Set text color to red for errors
        )
        return
    
    # Generate the expanded form using a list comprehension
    ls = [ch[i] + "0" * (len(ch) - i - 1) for i in range(len(ch)) if ch[i] != "0"]
    result = " + ".join(ls)  # Join the list of expanded values with " + "
    
    # Display the result in the label
    labelResult.config(text=result, fg="#333333")  # Set text color to dark gray for valid output

# Build the widgets for the GUI

# Header Label
header_label = Label(
    window,
    text="Write Number in Expanded Form",
    font=("Arial", 16, "bold"),  # Font styling
    bg="green",  # Green background
    fg="white",  # White text
    pady=10  # Padding around the text
)
header_label.grid(row=0, column=0, columnspan=2, sticky="nsew")  # Position the header

# Label for the input field
label_string = Label(
    window, 
    text="Enter a Number:", 
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

# Input field for the user to enter the number
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

# Button to trigger the expanded_form function
buttonResult = Button(
    window,
    text="Generate Expanded Form", 
    font=("Arial", 12, "bold"),  # Font styling
    bg="#2196F3",  # Blue background
    fg="white",  # White text
    command=expanded_form,  # Call the expanded_form function on click
    padx=5, 
    pady=5  # Padding inside the button
)
buttonResult.grid(
    row=2, 
    column=0, 
    columnspan=2,  # Span across two columns
    sticky="ew"  # Expand horizontally
)

# Label to display the expanded form of the number
labelResult = Label(
    window,
    text="",  # Initially empty
    font=("Courier", 14, "bold"),  # Font styling
    bg="#ffffff",  # White background
    fg="#333333",  # Dark gray text color
    bd=1,  # Border width
    relief="solid",  # Solid border style
    pady=10,  # Padding around the text
    wraplength=400  # Wrap text to fit within 400 pixels

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
