# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 20:01:46 2024

@author: admin
"""

import tkinter
from tkinter import *

btnWidth = 5
btnHeight = 5
btnBG = 'black'
btnFG = 'white'

def display0():
    newFormule = formule.get()
    formule.set(newFormule+"0")


def display1():
    newFormule = formule.get()
    formule.set(newFormule+"1")

def display2():
    newFormule = formule.get()
    formule.set(newFormule+"2")
    
def display3():
    newFormule = formule.get()
    formule.set(newFormule+"3")    

def display4():
    newFormule = formule.get()
    formule.set(newFormule+"4")


def display5():
    newFormule = formule.get()
    formule.set(newFormule+"5")

def display6():
    newFormule = formule.get()
    formule.set(newFormule+"6")


def display7():
    newFormule = formule.get()
    formule.set(newFormule+"7")

def display8():
    newFormule = formule.get()
    formule.set(newFormule+"8")

def display9():
    newFormule = formule.get()
    formule.set(newFormule+"9")

def displayAdd():
    newFormule = formule.get()
    formule.set(newFormule+"+")

def result():
    newFormule = formule.get()
    formule.set(newFormule+"1")
window = Tk()
window.title("sum of integers")
window.geometry("500x500")

#header message
labelMessage = Label(window,text="Sum of integers")
labelMessage.grid(row=0,column=6)

formule = StringVar()
enter = Entry(window,textvariable=formule)
enter.grid(row=1,column=6)
button0 = Button(window,text="0",bg=btnBG,fg=btnFG,width=btnWidth,height=btnHeight,command=display0)
button0.grid(row=2,column=0)
button1 = Button(window,text="1",bg=btnBG,fg=btnFG,width=btnWidth,height=btnHeight,command=display1)
button1.grid(row=2,column=1)
button2 = Button(window,text="2",bg=btnBG,fg=btnFG,width=btnWidth,height=btnHeight,command=display2)
button2.grid(row=2,column=2)

button3 = Button(window,text="3",bg=btnBG,fg=btnFG,width=btnWidth,height=btnHeight,command=display3)
button3.grid(row=3,column=0)
button4 = Button(window,text="4",bg=btnBG,fg=btnFG,width=btnWidth,height=btnHeight,command=display4)
button4.grid(row=3,column=1)
button5 = Button(window,text="5",bg=btnBG,fg=btnFG,width=btnWidth,height=btnHeight,command=display5)
button5.grid(row=3,column=2)

button6 = Button(window,text="6",bg=btnBG,fg=btnFG,width=btnWidth,height=btnHeight,command=display6)
button6.grid(row=4,column=0)
button7 = Button(window,text="7",bg=btnBG,fg=btnFG,width=btnWidth,height=btnHeight,command=display7)
button7.grid(row=4,column=1)
button8 = Button(window,text="8",bg=btnBG,fg=btnFG,width=btnWidth,height=btnHeight,command=display8)
button8.grid(row=4,column=2)

button9 = Button(window,text="9",bg=btnBG,fg=btnFG,width=btnWidth,height=btnHeight,command=display9)
button9.grid(row=5,column=0)
buttonAdd = Button(window,text="+",bg=btnBG,fg=btnFG,width=btnWidth,height=btnHeight,command=displayAdd)
buttonAdd.grid(row=5,column=1)
buttonEqual = Button(window,text="=",bg=btnBG,fg=btnFG,width=btnWidth,height=btnHeight,command=result)
buttonEqual.grid(row=5,column=2)

window.mainloop()










