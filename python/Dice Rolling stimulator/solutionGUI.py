# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 22:38:19 2024

@author: Rafik Ncib
"""

import tkinter
from tkinter import *

window = Tk()
window.geometry("400x400")

window.title("Dice Rolling")
import random

dice =["""
[-----------]
[           ]
[     0     ]
[           ]
[-----------]""",
"""
[-----------]
[  0        ]
[           ]
[        0  ]
[-----------]""",
"""
[-----------]
[  0        ]
[     0     ]
[        0  ]
[-----------]""",
"""
[-----------]
[  0     0  ]
[           ]
[  0     0  ]
[-----------]""",
"""
[-----------]
[  0     0  ]
[     0     ]
[  0     0  ]
[-----------]""",
"""
[-----------]
[  0     0  ]
[  0     0  ]
[  0     0  ]
[-----------]"""]


label = Label(window,text="Press Y if you want to roll the dice");
label.pack(pady=10)

def rollFunction():
    if(pressVariable.get().lower()=='y'):
        face = random.randint(1,6)
        label2.config(text=dice[face-1])
        label.config(text="Press Y if you want to roll the dice again")
        pressVariable.set("")
    else:
        label2.config(text="Enter 'Y' to roll the dice!")
        pressVariable.set("")
        
    
pressVariable = StringVar()
entry = Entry(window,textvariable=pressVariable)
entry.pack(pady=5)

button = Button(window,text="Roll",command=rollFunction)
button.pack(pady=5)

    




label2 = Label(window,text="", font=("Courier", 16), justify="center")
label2.pack(pady=20)





window.mainloop()
