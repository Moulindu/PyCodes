#Uses Python 3

import sys

def BinarySearch(A,l,r,k):    #l-> lower index & r-> upper index 

    if l>r:
        return -1           
    m=(l+r)//2
    #print(m)
    #print(A[m])

    if A[m]==k:
        return m
    else:
        if A[m]<k:
            return BinarySearch(A,m+1,r,k)
        else:
            return BinarySearch(A,l,m-1,k)


N = list(map(int, input().split()))     

M = list(map(int, input().split()))


#print(N[0])

#print(N[1:])

#assert(N[0]==len(N[1:]))

A = N[1:]


#print(M[0])

#print(M[1:])

#assert(M[0]==len(N[1:]))

B = M[1:]

for x in range(M[0]):
    print(BinarySearch(A,0,len(A)-1,B[x]),end=' ')











    

    
    
   
    
    
    
    
    
