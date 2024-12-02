# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 23:35:46 2024

@author: Rafik Ncib
"""

import tkinter
from tkinter import *

window = Tk()
window.geometry("400x400")

text = 'Programming in python.'
vowels = {'a', 'e', 'i', 'o', 'u'}

text = text.lower()

text = text.replace(' ','')

text = text.replace('.','')

newSet = {i for i in text}

newSet.difference_update(vowels)

count = len(newSet)
 
msg = f"Number of items: {count}"



label = Label(window,text=msg);
label.pack(expand=True)





window.mainloop()

