#Uses Python 3


def MoneyChange(n):
    A = list()
    A.extend([1,2,1,1])

    for i in range(4,n):
        count_1 = A[i-1]+1
        count_3 = A[i-3]+1
        count_4 = A[i-4]+1

        A.append(min(count_1,count_3,count_4))


    return A[n-1]

if __name__=='__main__':

    n = int(input())

    print(MoneyChange(n))
        
    

