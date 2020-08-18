# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 18:49:34 2020

@author: rm23m
"""
def smallest (a,b):
    if(a>b):
        print(a)
    elif(b>a):
        print(b)
    else:
        print("both are equal")

s= lambda x,y : x+y
difference= lambda x,y : x-y
n1=int(input("enter the fist number"))
n2=int(input("enter the second number"))
print("the smallest of two is ", smallest(s(n1,n2),difference(n1,n2)))
#%%
divide=lambda x,y :x/y
n1=int(input("enter num1 :"))
n2=int(input("enter num2 :"))
print(divide(n1,n2))
#%%
square=lambda x :x*x
n1=int(input("enter num:"))
print (square(n1))
#%%
def fun1(x,y,z=20):
    print (x,y,z)

fun1(25,75,55)
fun1(10,20)
#%%
def outerfun
   