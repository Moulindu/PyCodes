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
        


        
n = int(input())
P = Pisano(10)
if len(P)-2>n+2:
    if P[n+2] == 0:
        print(9)
    else:
        print(P[n+2]-1)
else:
    t = (n+2)%(len(P)-2)
    if P[t] == 0:
        print(9)
    else:
        print(P[t]-1)


    







    

