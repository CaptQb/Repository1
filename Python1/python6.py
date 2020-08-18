# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 11:34:04 2020

@author: rm23m
"""


str1="hello"
str2="how are you hello"
if str1 not in str2:
    print("present")
else:
    print("not presesnt")
#%%
str1="vi"
str2="victory"
if str1 in str2:
  print("present")
else:
  print("not present")    
#%%
str1="welcome to course on python"
p=0
for i in str1:
    if i in ['a','e','i','o','u']:
         print("present")
         break
p=p+1
#%%
str=input("enter the username: ")
for i in range(len(str)):
    new_string=()
