#Uses Python3
#!/usr/bin/python
import random

def Partition(A,key,l,r):
    #print(key)
    #print("low=",l,"high=",r)
    j = l-1
    k = j+1
    x = l
    m = j
    while x<=r:
        #print("Iteration:====")
        if A[x]<key:
            #print("x=",x)
            #print("j+1=",j+1)
            #print("k=",k)
            A[j+1],A[x]=A[x],A[j+1]
            #print("A=",A)
            if k!=j+1:
                A[x],A[k]=A[k],A[x]
                #print("A=",A)
            j=j+1
            k=k+1
            x=x+1
            m=m+1
        else:
            if A[x]==key:
                A[k],A[x]=A[x],A[k]
                #print("A=",A)
                k=k+1
                m=m+1
                x=x+1
            else:
                x = x+1

    

    return [j,k]
        
        





def QuickSort(A,l,r):
    #print("Iteration :====")
    if l>=r:
        return 

    key = random.choice(A[l:r+1])

    #print("pivot=",key)
    #print("A=",A)

    [m,n]= Partition(A,key,l,r)

    #print(A)

    QuickSort(A,l,m)
    QuickSort(A,n,r)


if __name__ == '__main__':
    n = int(input())
    A = list(map(int, input().split()))
    assert(n==len(A))
    QuickSort(A,0,n-1)
    print(*A)












    
        
    
    
    
    
    
                
            
