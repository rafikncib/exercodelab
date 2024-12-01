# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 22:39:58 2024

@author: Rafik Ncib
"""


import tkinter
from tkinter import *

window = Tk()
window.geometry("400x400")
window.title("ExercodeLab")
equal = '='*40

print(equal)
print("author: johnsmith@sample.com")
print("date: 01-01-2021")
print(equal)

labelEqualOne = Label(window,text=equal);
labelEqualOne.pack()

labelAuthor = Label(window,text="author: johnsmith@sample.com");
labelAuthor.pack()

labelDate = Label(window,text="date: 01-01-202");
labelDate.pack()

labelEqualTwo = Label(window,text=equal);
labelEqualTwo.pack()





window.mainloop()

