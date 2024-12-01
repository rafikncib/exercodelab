# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 22:54:58 2024

@author: Rafik Ncib
"""


import tkinter
from tkinter import *

window = Tk()
window.geometry("400x400")

pi = 3.14
radius = 5

area = pi*(radius **2)


msg = "Area: {}".format(area)

label = Label(window,text=msg);
label.pack()








window.mainloop()

