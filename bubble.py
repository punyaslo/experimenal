#!/usr/bin/python3

from array import *
x = array('i',[])

n = int(input("Enter the number of elements:"))
for i in range(n):
    print("Enter the next element")
    x.append(int(input()))

print("original array: ",str(x))

flag = False
for i in range(n-1):
    for j in range(n-1-i):
        if x[j] > x[j+1]:
           t = x[j]
           x[j] = x[j+1]
           x[j+1] = t
           flag = True
    
    if flag == False:
       break
    else:
       flag = False

print("The Sorted Array is:",x)
