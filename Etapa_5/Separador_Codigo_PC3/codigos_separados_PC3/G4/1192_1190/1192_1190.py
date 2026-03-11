from numpy import *

vet=array(eval(input("Informe o vetor: ")))


i=0
cont=0

while (i < size(vet)):
	if (vet[i] > 0):
		cont=cont+1
		
	i=i+1
	
x = linspace(vet[0], vet[-1], 5)
print(x)