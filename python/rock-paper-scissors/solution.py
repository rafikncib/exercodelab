# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 21:37:17 2025

@author: admin
"""

# Implement a basic rock-paper-scissors game for two players.

print("*"*7+"Rock paper scissors"+"*"*7+"\n")

print("*"*20)
print("1 : Rock")
print("2 : Paper")
print("3 : Scissors")
print("*"*20+"\n")

print("player 1 :")
while(True):
    user_input = input("Enter your choise: ")
    
    if user_input == "1":
        player1 = "Rock"
        break
    
    elif user_input == "2":
        player1 = "Paper"
        break
    
    elif user_input == "3":
        player1 = "Scissors"
        break
    
    else:
        print("Please choose one of this number 1, 2 or 3")
    

print("\nplayer 2 :")    
while(True):
    user_input = input("Enter your choise: ")
    
    if user_input == "1":
        player2 = "Rock"
        break
    
    elif user_input == "2":
        player2 = "Paper"
        break
    
    elif user_input == "3":
        player2 = "Scissors"
        break
    
    else:
        print("Please choose one of this number 1, 2 or 3")
        

print(f"player 1 chose {player1}")
print(f"player 2 chose {player2}")
if(player1==player2):
    print("it is a draw")
elif(player1 == "Rock" and player2=="Scissors")or(player1=="Scissors" and player2=="Paper") or(player1=="Paper" and player2=="Rock"):
    print("Player 1 wins.")
else:
    print("Player 2 wins.")