# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 09:58:13 2020

@author: rm23m
"""
import random
ch='y'
while ch=='y':
    opt=['rock','paper','scissor']
    a=int(input("player 1 enter your choice 0-rock 1 paper 2 scissor: "))
    b=random.randint(0,2)
    print("computer chose: ",opt[b])
    if (opt[a]=='rock' and opt[b]=='rock'):
     print("draw")
    elif(opt[a]=='rock'and opt[b]=='paper'):
     print("computer wins")
    elif(opt[a]=='rock'and opt[b]=='scissor'):
     print("player 1 wins")
    elif(opt[a]=='paper'and opt[b]=='rock'):
     print("player 1 wins")
    elif(opt[a]=='paper'and opt[b]=='paper'):
     print("draw")
    elif(opt[a]=='paper'and opt[b]=='scissor'):
     print("computer wins")
    elif(opt[a]=='scissor'and opt[b]=='rock'):
     print("computer wins")
    elif(opt[a]=='scissor'and opt[b]=='paper'):
     print("player 1 wins")
    elif(opt[a]=='scissor'and opt[b]=='scissor'):
     print("draw")
    print("wanna play again ?(y/n): ")
    ch=input("enter your choice: ")
    

    
 