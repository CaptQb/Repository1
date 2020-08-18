# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 19:18:02 2020

@author: rm23m
"""
#program to calculate Greatest Common divisor through recursion
def func(a,b):
    if(b==0):
        return a
    else:
        return func(b,a%b)
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
GCD=func(a,b)
print("GCD is: ")
print(GCD)
#%%
#Program to calculate exp(x,y) using recursive functions
def power(base,exp):
    if(exp==1):
        return(base)
    else:
        return (base*power(base,exp-1))
base=int(input("Enter the base number-"))
exp=int(input("Enter the exponential value-"))
print("Result:",power(base,exp))
#%%
#Program to print the Fibonacci series using recursion
def fibo(n):  
   if n <= 1:  
       return n  
   else:  
       return(fibo(n-1) + fibo(n-2))  
 
terms = int(input("How many terms? "))    
print("Fibonacci sequence:")  
for i in range(terms):  
    print(fibo(i)) 
#%%
#Program to find the number of times a recursive function is called
count=0
def fact(num):
    if (num==1 or num==0):
        return 1
    else:
        global count
        count=count+1
        return (num * fact(num-1))
            
n1=int(input("enter num: "))
n=fact(n1)
print(n,"\nnumber of times this program runs is ",count)
#%%
#Program to concatenate two strings using recursion
#creating random password pin
import random
def func(str):
    alph = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*(){}[]<>,.')
    str+=random.choice(''.join(alph))
    return str
result=''
for i in range (10):
    result=func(result)
print(result)    
    
    
#%%
#Write a menu driven program using functions to perform calculator
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y   
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
choice=int(input("enter your choice : "))
if choice == 1:
            print(num1, "+", num2, "=", add(num1, num2))
elif choice == 2:
            print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == 3:
            print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == 4:
            print(num1, "/", num2, "=", divide(num1, num2))
#%%
#Write a lambda function that finds the smallest of two numbers
small= lambda x,y:x if (x<y) else y 
n1=int(input("enter 1st number :"))
n2=int(input("enter 2nd number :"))
x=small(n1,n2)
print(x) 
#%%
#Write a program to compute lambda(n) for all positive values of n where lambda(n) can be recursively defined as lambda(n) = lambda(n/2) +1 if n>1
#doubt in this program
func=lambda x:0 if x<=1 else func(x/2)+1  
n1=int(input("enter the starting value: "))
ans=func(n1)
print(ans)           