#Uses Python 3

def PrimitiveCalculator(A,n):
    
    A.extend([0,1,1])
    for i in range(3,n):
        count_1 = A[i-1]+1
        if (i+1)%2==0:
            count_2 = A[((i+1)//2)-1]+1
        else:
            count_2 = count_1

        if (i+1)%3==0:
            count_3 = A[((i+1)//3)-1]+1
        else:
            count_3 = count_1

        A.append(min(count_1,count_2,count_3))

    return A


def Show_Intermediate_Nums(A,n):

    m = A[n-1]

    B = list()

    B.append(n)

    x = n-1

    for i in range(1,m):

        if A[x-1]+1== A[x]:
            B.append(x)
        else:
            if (x+1)%2==0 and A[((x+1)//2)-1]+1==A[x]:
                B.append((x+1)//2)
            else:
                if (x+1)%3==0 and A[((x+1)//3)-1]+1== A[x]:
                    B.append((x+1)//3)
        x = B[i]-1

    B.append(1)    

    B = sorted(B)
    print(*B)


if __name__=='__main__':
    n = int(input())
    A = list()

    A = PrimitiveCalculator(A,n)

    print(A[n-1])

    Show_Intermediate_Nums(A,n)
        
        
        
        
    
    
