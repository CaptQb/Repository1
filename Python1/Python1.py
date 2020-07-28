# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 18:04:31 2020

@author: rm23m
"""
#program to print factorial of a number
num=int(input("enter the number: "))
factorial=1
for i in range(1,num + 1):
       factorial = factorial*i
print("The factorial of",num,"is",factorial)

#%%

#program to check if a number is prime or composite    
num=int(input("enter the number: "))  
for i in range(2,num):
       if (num % i) == 0:
           count=1
           break
       else:
           count=0
if(count==0):
    print("prime")
else:
    print("composite")

#%%

#program to calculate sum of series 1+1/2+1/3...

num=int(input("enter the number upto n: "))
sum=0
for i in range(1,num+1):
    sum=sum+1/i
print("sum of series 1+1/2+...1/n is ",sum)

#%%

#program to print calender for a month
starting_day=int(input("enter the starting day 1=sat 2=mon 3= tues and so on : "))
total_days=int(input("enter the total number of days in that month : "))
print("Sun\tMon\tTues\tWed\tThu\tFri\tSun")
date=1
if(starting_day>0 and starting_day<8 and total_days<32 and total_days>27):
 for i in range(1,total_days+starting_day):
        if(i<starting_day):
            print("",end="\t")
        else:
            print(date,end="\t")
            date=date+1
        if(i%7==0):
            print("\n")
else:
 print("wrong input values")        

#%%
 
#program to print a pattern 

arr=[1,2,3,4,5] 
for i in range(0,6):
    for j in range(0,i):
        print(arr[j],end="")
    print("\n")    

#%%

#program on list tuple and dictionary

lst=[1,2,3,4,5]
lst1=(1,2,3,4,5)
lst2={'keyword',2,'words'}
lst3=[6,7,8,9]
print(type(lst))
print(type(lst1))
print(type(lst2)) 
print(lst[2:3]) 
print(lst+lst3)

