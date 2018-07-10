#Uses Python3


def finalnum(n):
    i=10
    while True:
        k = n%i
        if k==n:
            if i==10:
                return n
            else:
                return(n-p)//(i//10)
        p = k
        i = i*10



def largest(B):

    key=finalnum(B[0])
    c=0
    for i in range(1,len(B)):
        if finalnum(B[i])>key:
            c = i
            key = finalnum(B[i])

    B[0],B[c]=B[c],B[0]

    return B

def 

m = int(input())

B = [int(x) for x in input().split()]

assert(m==len(B))

B = sorted(B, reverse = True)

M = len(B)

for i in range(M):
    #print(i+1)
    B[i:]= largest(B[i:])
    #print(B)
    



for i in range(M):
    print(B[i],end='')




    

    
