# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 09:57:00 2020

@author: rm23m
"""
#Rishabh Mittal

def outerfun(a,b):
    def innerfun(c,d):
        return c+d
    return innerfun(a,b)

res=outerfun(5,10)
print(res)
#%%
def fun1(num):
    return(num+25)

n=fun1(5)
print(n)
#%%
def fun1(num):
    return num+2,num+3
#%%
def display(**kwargs):
    for i in kwargs:
        print(i)
        
display(emp="kelly",salary=9000)
#%%
def outer(a1,b1):
    def inner(c1,d1):
        return c1+d1
    return(a1)
    return inner(a1,b1)
    
 
n=outer(5,10)
print(n)