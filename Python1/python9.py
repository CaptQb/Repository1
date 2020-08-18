# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 10:40:28 2020

@author: rm23m
"""


str=input("enter the string: ")
str2=str.lower()
words=str2.split()
print("Duplicate words in the given string :")
for i in range(0,len(str2)):
    count=1
    for j in range(i+1,len(words)):
        if(words[i]==words[j]):
            count=count+1
           
    if(count>1 and words[i]!="0"):
        print(words[i],count)
#%%
        l1=list()
        l1.append([1,[2,3],4])
        l1.extend([7,8,9])
        print(l1[0][1][1]+l1[2])