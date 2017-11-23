#!/usr/bin/python3

max = int(input("Enter the max number upto which prime numbers would be estimated:"))

for num in range(2,max+1):
    for i in range(2,num):
        if num%i == 0:
           break;
    else:
        print(num,end=' ')
else:
    print()
