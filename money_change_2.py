#Uses python3


D = [10,5,1]

m = int(input())


i =0
v=0

while i<= 2:
    if D[i]<=m:
        #print(D[i])
        r = m%D[i]
        #print(r)
        k = (m-r)//D[i]
        #print(k)
        v = v+k
        #print(v)
        
        if r==0:
            break
        else:
            m=r
                
                
    i=i+1
   

print(v)
