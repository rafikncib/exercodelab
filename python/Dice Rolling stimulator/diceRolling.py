# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 13:31:02 2024

@author: Rafik Ncib
"""


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


y = input("press Y if you want to roll the dice")

while(y.lower()=='y'):
    face = random.randint(1,6)
    print(dice[face-1])
    y = input("press y if you want to roll the dice again")
