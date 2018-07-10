#!/usr/bin/python

import random

import QuickSort




X=0


while X<=10000:
    print("Iteration: ",X+1)
    n = random.choice(range(1,1000))
    #print("n=",n)
    A = list()
    for i in range(n):
        A.append(random.choice(range(1,10000)))

    #print("A=",A)

    B = sorted(A)
    QuickSort.QuickSort(A,0,n-1)

    if B!=A:
        print("error")
        print ("A=", A)
        print ("n=", n)
        break
    else:
        X = X+1
        continue


    




   



