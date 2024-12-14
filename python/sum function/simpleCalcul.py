# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 20:01:46 2024

@author: Rafik Ncib
"""

import tkinter
from tkinter import *

btnWidth = 7
btnHeight = 7
btnBG = 'white'
btnFG = 'black'

buttonList =[
    {"textValue":"9","row":3,"column":2},
    {"textValue":"8","row":3,"column":1},
    {"textValue":"7","row":3,"column":0},
    
    {"textValue":"6","row":4,"column":2},
    {"textValue":"5","row":4,"column":1},
    {"textValue":"4","row":4,"column":0},
    
    {"textValue":"+","row":5,"column":3},
    {"textValue":"3","row":5,"column":2},
    {"textValue":"2","row":5,"column":1},
    {"textValue":"1","row":5,"column":0},
    
    {"textValue":"=","row":6,"column":3},
    {"textValue":",","row":6,"column":2},
    {"textValue":"0","row":6,"column":1},
    {"textValue":"+/-","row":6,"column":0},
    
    
    
]
def display(t):
    newFormule = formule.get()
    lengthFormule = len(newFormule)
    print(newFormule,lengthFormule)
    if(newFormule!="0"):
        formule.set(newFormule+t)
    else:
        formule.set(t)

def result():
    newFormule = formule.get()
    
    try:
        res = eval(newFormule)
        formule.set(res)
    except Exception:
        print("Errrrrrreeeeeur")
    
window = Tk()
window.title("sum of integers")

# Configure rows and columns to resize dynamically
window.grid_rowconfigure(0, weight=1)
for i in range(7):  # Adjust for the number of rows
    window.grid_rowconfigure(i, weight=1)
for i in range(4):  # Adjust for the number of columns
    window.grid_columnconfigure(i, weight=1)
    
formule = StringVar(value="0")
enter = Label(window,textvariable=formule,bg="lightgrey",
    anchor="e",
    font=("Arial", 20),
    height=2  # Make it taller to display "0" properly
    )
enter.grid(row=0,column=0, columnspan=4, sticky="nsew")
for btn in buttonList:
    print(btn)
    if(btn["textValue"]==","):
        button = Button(window,text=btn['textValue'],bg=btnBG,fg=btnFG ,font=("Arial", 18),command=lambda t="." :display(t))
    elif(btn["textValue"]=="="):
        button = Button(window,text=btn['textValue'],bg=btnBG,fg=btnFG,font=("Arial", 18),command=result)
    else:
        button = Button(window,text=btn['textValue'],bg=btnBG,fg=btnFG,font=("Arial", 18),command=lambda t=btn['textValue'] :display(t))
    button.grid(row=btn['row'],column=btn["column"], sticky="nsew")
        

window.mainloop()










