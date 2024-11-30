# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 12:37:37 2024

@author: Rafik Ncib
"""

import tkinter
from tkinter import *

window = Tk()
window.geometry("400x400")

label = Label(window,text="your age");
label.pack()

age = StringVar()
entry = Entry(window,textvariable=age)
entry.pack()



def display():
    label2.config(text="I am {} years old.".format(age.get()))
    
button = Button(window,text="display age",command=display)
button.pack()


label2 = Label(window)
label2.pack()

window.mainloop()
