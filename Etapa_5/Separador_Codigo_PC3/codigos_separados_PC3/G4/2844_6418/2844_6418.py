from numpy import *

A = array(eval(input()))
j = 0
for i in A:
	A[j]= i - 1
	if A[j]== -1:
		A[j]=9
	j+=1
print(A)