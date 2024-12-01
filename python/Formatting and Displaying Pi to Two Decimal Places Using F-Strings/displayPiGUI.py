# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 22:30:52 2024

@author: Rafik Ncib
"""

import tkinter
from tkinter import *

window = Tk()
window.geometry("400x400")

pi = 3.1415926535

print("Pi: {:.2f}".format(pi))

msgPriceWeight = "Pi: {:.2f}".format(pi)

label = Label(window,text=msgPriceWeight);
label.pack()








window.mainloop()