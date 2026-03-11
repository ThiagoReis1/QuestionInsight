from numpy import *
vet=array(eval(input("Informe o vetor de numeros reais: ")))
i=0
m=0
total=0

while i<size(vet):
	m=m+vet[i]**2
	i=i+1
	
total=(m/size(vet))**(1/2)

print(round(total, 2))
	