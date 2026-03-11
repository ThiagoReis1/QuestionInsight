from numpy import *
A = array(eval(input("Entrada: ")))
n = 0 #numero de saques <= 50

for i in arange(size(A)):
	if A[i] <= 50.00:
		n = n + 1

B = zeros(n, dtype = int)
C = arange(size(A))
n = 0


for i in C:
	if A[i] <= 50.00:
		B[n] = C[i]
		n = n + 1
		
print(n)
print(B)
