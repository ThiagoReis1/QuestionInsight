from numpy import*

N = int(input(": "))

mat = zeros((N,N),dtype=int)

for i in range (N):
	for j in range (N):
		if(i>j):
			mat[i,j]=0
		else:
			mat[i,j]=1
			
print(mat)
	