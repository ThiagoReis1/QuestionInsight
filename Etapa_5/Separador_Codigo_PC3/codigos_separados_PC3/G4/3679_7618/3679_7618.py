from numpy import *

n=int(input("numero: "))


mat=ones((n,n), dtype=int)

for i in range(n):
	for j in range(n):
		if i > j:
			mat[i,j]= 0
			
print(mat)
			