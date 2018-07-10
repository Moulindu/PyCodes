#Uses Python3

n = int(input())

A = list()



S=1

x=0

A.append(1)

while S<=n:
    #print(x+1,":")
    A.append(A[x]+1)
    #print(A)
    S = S+A[x]+1
    #print(S)
    x+=1

print(x)
A = A[0:x-1]
#print(A)
A.append(n-sum(A))
#print(A)
#print(len(A))

for i in range(len(A)):
    print(A[i],end=' ')
