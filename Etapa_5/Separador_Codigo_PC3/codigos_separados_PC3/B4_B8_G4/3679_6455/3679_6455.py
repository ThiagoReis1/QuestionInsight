from numpy import *
N = int(input("Digite um numero: "))
mat = zeros((N,N), dtype = int)

for i in range(shape(mat)[0]):
	for j in range(shape(mat)[1]):
		if(i == j):
			mat[i,j] = 1
		elif(i < j):
			mat[i,j] = 1
		elif(i > j):
			mat[i,j] = 0
print(mat)