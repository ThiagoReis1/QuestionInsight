from numpy import*
from numpy.linalg import*
from math import*
vet=array(eval(input("digite a matriz: ")))
vet1=zeros(size(vet),dtype=float)

for i in range (size(vet)):
	if (vet[i]>80):
		vet1[i]=vet[i]-vet[i]*15/100
	else:
		vet1[i]=vet[i]
soma=sum(vet1)
print(round(soma,2))

