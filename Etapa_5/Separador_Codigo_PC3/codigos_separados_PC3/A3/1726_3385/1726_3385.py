from numpy import*

matriz_notas=array= (eval(input("m:")))
lin= shape (matriz_notas)[0]
col= shape (matriz_notas)[1]
menor=9999999999999999999999
indices=3
for i in range(lin):
	for j in range (col):
		if matriz_notas[i][j]<menor:
			indice=i
			menor=matriz_notas[i][j]
		else:
			j=j+2
print(menor)