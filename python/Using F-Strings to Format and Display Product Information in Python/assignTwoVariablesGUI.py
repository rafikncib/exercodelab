# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:56:43 2024

@author: admin
"""

import tkinter
from tkinter import *

window = Tk()
window.geometry("400x400")

price = 34.99
weight = 20
 
msgPriceWeight = f'Price: ${price}. Weight: {weight} lbs.'

label = Label(window,text=msgPriceWeight);
label.pack()








window.mainloop()