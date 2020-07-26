# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 22:16:29 2020

@author: rm23m
"""
#program to calculate area of a circle
r=float(input("enter the radius : "))
print("the area of circle is : ", 3.14*r*r)
#%%
#program to calculate area of triangle
a= float(input("Enter first side"))
b= float(input("Enter second side"))
c= float(input("Enter third side"))
s = (a+b+c)/2
area= (s*(s-a)*(s-b)*(s-c)) ** 0.5
print("the area of the triangle is ", area)
#%%
#program to claculate the distance between two points
x1=int(input("enter x cordinate of 1st point"))
y1=int(input("enter y cordinate of 1st point"))
x2=int(input("enter x cordinate of 2st point"))
y2=int(input("enter y cordinate of 2st point"))
distance=((y2-y1)**2 + (x2-x1)**2)**0.5
print(distance)
#%%
#program to claculate the bill of an purchase
a=int(input("amount of item sold :"))
p=int(input("enter the price of a single item"))
d=int(input("enter the % of discount : "))  
total=a*p
tax=total*18/100
bill=total+tax-((total+tax)*d/100)
print(bill)
#%%
#program to claculate the result 
exam1=int(input("enter the exam1 score :"))
exam2=int(input("enter the exam2 score :"))
sport=int(input("enter the sports score :"))
act1=int(input("enter activity1 score :"))
act2=int(input("enter activity2 score :"))
act3=int(input("enter activity3 score :"))
examination=(exam1+exam2)/2
activity=(act1+act2+act3)/3
result=(examination*.5 + sport*.2 + activity*.3)
print(result)
#%%
#program to check the case of a character
ch=input("enter a character : ")
if (ch >= 'A' and ch <= 'Z'): 
  print(ch,"is an UpperCase character");
  print(ch.lower())
elif (ch >= 'a' and ch <= 'z'): 
  print(ch,"is an LowerCase character"); 
  print(ch.upper())
else: 
  print(ch,"is not an aplhabetic character");
#%%
#program to swap two numbers  
x=int(input("enter the first number"))
y=int(input("enter the first number"))
print("before swapping the x is ",x," the y is ",y)
temp = x
x = y
y = temp
print("after swapping x is ",x, "y is ",y)
#%%
#program to tell total time in a day in seconds
time=24*60*60
print("total time in second in a day is ",time)
#%%
#program to calculate the momentum of a body
m=float(input("enter the mass in kg :"))
c=float(input("enter the velocity in m/s :"))
momentum=m*c*c
print("its momentum is ",momentum)    