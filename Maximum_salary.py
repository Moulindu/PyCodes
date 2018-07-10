#Uses Python3

def Split(n):
    A = list()
    B = list()
    B.append(n%10)
    i = 10
    count = 0
    while True:
        #print(i)
        k = n%i
        #print(k)
       
        if k==n:
            if i == 10:
                A.append(n)
                #print(A)
            else:
                A.append((k-B[count-1])//(i//10))
            break
            
                    
            
            
        else:
            if i==10:
                A.append(k)
            else:
                A.append((k-B[count-1])//(i//10))
                #print(A)
        i = i*10
        count +=1
        B.append(A[count-1])

    return(A)

def largest(B):

    key=B[0]
    c=0
    for i in range(1,len(B)):
        if B[i]>key:
            c = i
            key = B[i]

    B[0],B[c]=B[c],B[0]

    return B
    


m = int(input())

A = [int(x) for x in input().split()]

B = list()

assert(len(A) == m)

for i in range(m):
    B.extend(Split(A[i]))



M = len(B)

key = B[0]

for i in range(M):
    #print(i+1)
    B[i:]= largest(B[i:])
    #print(B)

for i in range(M):
    print(B[i],end='')




             
    


