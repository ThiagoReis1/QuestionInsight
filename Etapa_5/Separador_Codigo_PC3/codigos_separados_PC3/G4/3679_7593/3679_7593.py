from numpy import*
B = int(input("N: "))
N = zeros((B,B),dtype = int)

for  i in range(B):
	for j in range(B):
		if ( i <= j):
			N[i,j]=1
print(N)