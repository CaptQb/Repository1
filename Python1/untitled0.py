# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 18:04:31 2020

@author: rm23m
"""
# Program to calculate average of n numbers
num = int(input('How many numbers: '))
total_sum = 0.
for n in range(0,num):
  numbers = float(input('Enter number : '))
  total_sum += numbers
avg = total_sum/num
print('Average of ', num, ' numbers is :', avg)

#%%

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
starting_day=int(input("enter the starting day"))
total_days=int(input("enter the total number of days in that month"))
