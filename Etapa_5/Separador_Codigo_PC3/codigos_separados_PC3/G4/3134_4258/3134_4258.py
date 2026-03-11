from numpy import *

vet = array(eval(input("Vetor de n numeros positivos: ")))
i = 0
n = size(vet)
s = 0

while(i < n):
	s = s + ((vet[i])**2)
	i = i + 1
	
m =  ((s/n)**0.5)
print(round(m, 2))