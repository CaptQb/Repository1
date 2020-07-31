# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 10:46:46 2020

@author: rm23m
"""


def func(x):
    factorial=1 
    for i in range(1,x + 1):
       factorial = factorial*i
    print("The factorial of",x,"is",factorial)

num=int(input("enter the number :"))
func(num)    
#%%
def func(x,x1,x2,x3,x4):
    avg=(x+x1+x2+x3+x4)/5
    print(avg)

x=int(input("enter the marks of 1st :"))
x1=int(input("enter the marks of 2nd :"))
x2=int(input("enter the marks of 3rd :"))
x3=int(input("enter the marks of 4th :"))
x4=int(input("enter the marks of 5th :"))
func(x,x1,x2,x3,x4)    

#%%
def func():
    a=int(input("enter the number"))
    print("its cube is : ", a*a*a)

func()
#%%
def func(a):
    print("the cube of ",a,"is ",a*a*a)

num=int(input("enter the number : "))
func(num)
#%%
def func():
    a=int(input("enter the radius :"))
    print("its area is : ", 3.14*a*a)

func()
#%%
def func(a):
    print("the area is ",3.14*a*a)

num=int(input("enter the radius of the circle : "))
func(num)
#%%
def func():
    a=int(input("enter the start : "))
    b=int(input("enter the end : "))
    sum=0
    for i in range (a,b+1):
        sum=sum+i
    print("sum is : ", sum)

func()
#%%
def func(a,b):
    sum=0
    for i in range (a,b+1):
        sum=sum+i
    print("sum is : ", sum)

x=int(input("enter the start : "))
y=int(input("enter the end : "))
func(x,y)
func(2,9)
#%%
def func(a=5,b=9):
    sum=0
    for i in range (a,b+1):
        sum=sum+i
    print("sum is : ", sum)

func(1,9)
#%%
def func(a,b):
    print(a+b)

x=input("enter the first string :")
y=input("enter the second string :")
func(x,y)
func("my","name")
#%%
def func(a="hello",b="world"):
    print(a+b)

x=input("enter the first string :")
y=input("enter the second string :")
func(x,y)    