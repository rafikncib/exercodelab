# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 22:34:02 2024

@author: Rafik Ncib
"""

import tkinter
from tkinter import *

window = Tk()
window.geometry("400x400")

dash="-"*40

msg = "{}\nVERSION: 1.0.1\n{}".format(dash,dash)

label = Label(window,text=msg);
label.pack()








window.mainloop()