# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:51:52 2024

@author: admin
"""

import tkinter
from tkinter import *

window = Tk()
window.geometry("400x400")
window.title("Assign a Price")
price = 69.99
 
msgPrice = f"This costs {price}"
label = Label(window,text=msgPrice);
label.pack(expand=True)








window.mainloop()