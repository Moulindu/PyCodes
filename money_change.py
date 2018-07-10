#Uses python3


D = [10,5,1]

m = int(input())


i =0
v=0

while i<= 2:

    X = m-D[i]
    
    if X>=0:
        t = 1
        
        while True:
            
            X = m-(D[i]*t)
            if X<0:
                m = m - (D[i]*(t-1))
                break
            else:
            
                
                t=t+1
                v=v+1
                
                
    i=i+1
   

print(v)
    
            
