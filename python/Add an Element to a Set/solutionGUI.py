# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 22:57:10 2024

@author: Rafik Ncib
"""

import tkinter
from tkinter import *

window = Tk()
window.geometry("400x400")

subjects = {'mathematics', 'biology'}

subjects.add("english")



label = Label(window,text=subjects);
label.pack(expand=True)





window.mainloop()