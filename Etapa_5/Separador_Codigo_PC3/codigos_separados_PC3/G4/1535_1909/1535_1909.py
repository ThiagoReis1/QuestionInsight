from math import*
X = float(input())
K = int(input())
I=1
A = X
while(I < K): 
	A = A + (X**(I+2)/I+2) * (-1)**(I)
	I = I + 1
print(round(A,6))