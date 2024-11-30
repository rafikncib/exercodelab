# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 13:14:50 2024

@author: Rafik Ncib
"""



import tkinter
from tkinter import *

window = Tk()
window.geometry("400x400")

lang = "Python"
version = "3.8"
 
msg = "I am learning {} version {}".format(lang,version)
label = Label(window,text=msg);
label.pack()








window.mainloop()