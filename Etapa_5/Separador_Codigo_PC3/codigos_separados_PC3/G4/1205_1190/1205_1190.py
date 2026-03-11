from numpy import *

vet=array(eval(input("Informe o vetor: ")))
recorde=8.95

i=0
cont=0
print(recorde)
while (i < size(vet)):
	if (vet[i] > recorde):
		cont=cont+1
		
	i=i+1
print(cont)