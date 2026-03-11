from numpy import*
from numpy.linalg import*


vet=array(eval(input()))
aux=size(vet)
cont = 0 
for i in range(aux):
	if(vet[i]>=vet[0] and i!=0):
		print(i)
		cont=cont+1
		
print(cont)