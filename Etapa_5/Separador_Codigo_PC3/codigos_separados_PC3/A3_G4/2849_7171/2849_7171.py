#reinicio
from numpy import*

vet=array(eval(input("Digite o vetor notas:")))
soma=0

for i in vet:
	if (i!=0):
		soma= soma + i
	else:
		soma= 0
print(soma)