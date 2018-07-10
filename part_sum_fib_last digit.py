# Uses python3


def Pisano(m):
    P = [0,1]
    a = 0
    b = 1
    while True:
        c = (a+b)%m
        P.append(c)
        a,b = b,c
        if a==0 and b==1:
            break
    return P


[m,n]= [int(x) for x in input().split()]


    

P=Pisano(10)

t = len(P)-2

if m==n:
    r = (m+1)%t
    print(P[r-1])

else:
    Q1 = (m+1)//t
    Q2 = (n+1)//t
    R1 = (m+1)%t
    R2 = (n+1)%t
    S = (Q2-Q1)*sum(P[0:t]) + sum(P[0:R2]) - sum(P[0:R1-1])
    print(S%10)


    

    

    

   





    
    
