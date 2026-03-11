from numpy import*
n=int(input("Digite um numero: "))

matriz=ones((n,n),dtype=int)
for i in range(matriz.shape[0]):
	for j in range(matriz.shape[1]):
		if	i > j:
			matriz[i,j]=0
		
print(matriz)
	