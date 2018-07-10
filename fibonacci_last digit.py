# Uses python3

F = list()

n = int(input())

F.extend([0,1])

for x in range(2,n+1):
    F.append((F[x-1]+F[x-2])%10)

   


print(F[n])
    
