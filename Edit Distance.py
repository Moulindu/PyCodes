#Uses Python 3

# It will return the D-matrix
def EditDistance(A,B):

    m = len(A)
    n = len(B)

    X = list()
    Y = list()

# '0' or any specific character is added to the beginning of the lists
    X.append(0)
    Y.append(0)

    X.extend(A)
    Y.extend(B)

    

    
# D is initialized
    D = [[0 for x in range(m+1)] for y in range(n+1)]

  #The first row and first column of D is being re-initialized
    for i in range(n+1):           
        D[i][0]= i

    for j in range(m+1):
        D[0][j]=j


#Filling in the values of D
    for j in range(1,m+1):
        for i in range(1,n+1):
            #print("Interation:")
            
            

            
            if X[j]!=Y[i]:                
                insertion = D[i-1][j]+1
                deletion = D[i][j-1]+1
                mismatch = D[i-1][j-1]+1
                D[i][j]= min(insertion,deletion,mismatch)

            else:
                D[i][j] = D[i-1][j-1]
            #print("D[",i,"]","[",j,"]=",D[i][j])

    return D[n][m]


if __name__=='__main__':

    A = input()

    B = input()

    print(EditDistance(A,B))


  

    
