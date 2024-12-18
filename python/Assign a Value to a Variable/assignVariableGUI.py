# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:47:40 2024

@author: admin
"""

import tkinter
from tkinter import *

window = Tk()
window.geometry("400x400")
window.title("Assign a Variable")

price = 199.99
 
msgPrice = "This costs {}".format(price)
label = Label(window,text=msgPrice);
label.pack(expand=True)








window.mainloop()