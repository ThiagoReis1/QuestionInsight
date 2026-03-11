from numpy import *

vet = array(eval(input("Digite os valores: ")))
soma = 200
i = 0

while(i < size(vet)):
	if(vet[i] == 1):
		soma = soma / 2
	if(vet[i] == 2):
		soma = soma * 3
	if(vet[i] == 3):
		soma = soma / 2
	if(vet[i] == 4):
		soma = soma * 3
	if(vet[i] == 5):
		soma = soma / 2
	if(vet[i] == 6):
		soma = soma * 3
		
	i += 1
	
print(round(soma, 2))