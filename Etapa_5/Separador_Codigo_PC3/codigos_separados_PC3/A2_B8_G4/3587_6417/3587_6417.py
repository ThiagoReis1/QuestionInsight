from numpy import *

vet = array(eval(input("Numeros do vetor: ")))

i = 0
soma = 100

while i < size(vet):
	if(vet[i] == 1):
		soma = soma * 5
		
	elif(vet[i] == 2):
		soma = soma* 3
	
	elif(vet[i] == 3):
		soma = soma
		
	elif(vet[i] == 4):
		soma = soma / 2
	
	i = i + 1
	
print(round(soma,2))