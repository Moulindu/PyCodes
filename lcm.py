#Uses python3

import sys
def gcd(a,b):

        if a<b:
                a,b = b,a
                
        c=a%b

        if c==0:
                return b
        else:
                a=b
                b=c
        return gcd(a,b)
                
	

	
		


	


inp = sys.stdin.read()

A = inp.split()

a = int(A[0])
b = int(A[1])

print((a*b)//gcd(a,b))
	
