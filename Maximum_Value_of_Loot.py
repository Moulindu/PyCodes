#Uses Python3

from operator import itemgetter


[n,W] = [int(x) for x in input().split()]

A = list()

for x in range(n):
    [a,b]= [int(x) for x in input().split()]
    A.append([a,b])


for x in range(n):
    A[x-1][0] = A[x-1][0]/A[x-1][1]


A = sorted(A, key = itemgetter(0),reverse = True)

#print(A)

V = 0

for x in range(1,n+1):
    #print(x,":/n")
    if A[x-1][1]<W:
        V = V + (A[x-1][1]*A[x-1][0])
        #print(V)
        W = W - A[x-1][1]
        #print(W)
        #if W==0:
            #break
    else:
        V = V +(W*A[x-1][0])
        break

print(round(V,4))

    
        
        
    




    






