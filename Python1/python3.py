# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 10:46:46 2020

@author: rm23m
"""


def func(num):
    factorial=1 
    for i in range(1,num + 1):
       factorial = factorial*i
    print("The factorial of",num,"is",factorial)
num=int(input("enter the number :"))
func(num)    