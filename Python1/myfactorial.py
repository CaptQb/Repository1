# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 10:34:29 2020

@author: rm23m
"""
def fact(num):
    if (num==1 or num==0):
        return 1
    else:
        return (num * fact(num-1))
    
n1=int(input("enter num: "))
n=fact(n1)
print(n)
