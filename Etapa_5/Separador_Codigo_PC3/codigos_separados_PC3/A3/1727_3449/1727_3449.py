from numpy import*
from numpy.linalg import*
n=array(eval(input("notas:")))
lin= shape(n)[0]
col= shape(n)[1]
maior=0
indice=0

for i in range(lin):
	for j in range(col):
		if n[i][j]> maior:
			indice =i
			maior = n[i][j]
		else:
			j=j+1
print(maior)