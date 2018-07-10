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
        


n,m = [int(x) for x in input().split()]

P = Pisano(m)

if len(P)-2>n:
    print(P[n])

else:
    t = n%(len(P)-2)
    print(P[t])
        
   



    
