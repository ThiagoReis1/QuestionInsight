from numpy import*
from numpy.linalg import*
matriz=array(eval(input("digite a matriz: ")))
vet=zeros(matriz.shape[0],dtype=float)

for i in range(matriz.shape[0]):
	vet[i]=min(matriz[i])
mv=min(vet)
for x in range(size(vet)):
	if vet[x]==mv:
		print(x)
	
	