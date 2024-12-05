# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 19:32:56 2024

@author: Rafik Ncib
"""

import tkinter
from tkinter import *

window = Tk()
window.geometry("400x400")

window.title("Even or Odd")


label = Label(window,text="Even or Odd")
label.pack(pady=10)


def even_or_odd():
    if(len(number.get())==0):
        label2.config(text="Input is empty! Please enter a number.")
        number.set("")  # Clear the input field
        return
    try:
        nbre = int(number.get())
        if(nbre%2==0):
            label2.config(text=f"{nbre} is Even")
            number.set("")
        else:
            label2.config(text=f"{nbre} is Odd")
            number.set("")
    except Exception:
        label2.config(text=f"{number.get()} is not a number")
        number.set("")
    
number = StringVar()
entry = Entry(window,textvariable=number)
entry.pack(pady=5)

button = Button(window,text="Verify",command=even_or_odd)
button.pack(pady=5)

    

label2 = Label(window,text="", font=("Courier", 12), justify="center")
label2.pack(pady=20)




window.mainloop()