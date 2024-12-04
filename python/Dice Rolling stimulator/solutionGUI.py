# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 22:38:19 2024

@author: Rafik Ncib
"""

import tkinter
from tkinter import *

window = Tk()
window.geometry("400x400")

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


label = Label(window,text="press Y if you want to roll the dice");
label.pack()

def rollFunction():
    if(pressVariable.get().lower()=='y'):
        face = random.randint(1,6)
        label2.config(text=dice[face-1])
        
    
pressVariable = StringVar()
entry = Entry(window,textvariable=pressVariable)
entry.pack()
button = Button(window,text="Roll",command=rollFunction)
button.pack()

    




label2 = Label(window)
label2.pack()





window.mainloop()
