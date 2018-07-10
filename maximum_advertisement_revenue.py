#Uses python3

n = int(input())

A = list()
B = list()

A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

assert(len(A)==len(B)==n)

A = sorted(A, reverse = True)

B = sorted(B, reverse = True)

S=0

for i in range(n):

    S = S + A[i-1]*B[i-1]


print(S)
    
