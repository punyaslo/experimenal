#!/usr/bin/python3
max = int(input("Enter the number of items you want"))

f1=0
f2=1

if max == 1:
   print(f1)

if max == 2:
   print(f1,f2,sep='\n',end='\n')

count=2
if max > 2:
   print(f1,f2,sep='\n',end='\n')

   while count < max:
         f=f1+f2
         print(f)
         f1,f2=f2,f
         count=count+1
