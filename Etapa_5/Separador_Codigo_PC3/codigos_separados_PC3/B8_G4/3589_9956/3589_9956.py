from numpy import*

i=0
soma=0

vet = array(eval(input()))

while i < size(vet):
	if vet[i] == 1:
		soma = soma + 80
	elif vet[i] == 2:
		soma = soma + 40
	elif vet[i] == 3:
		soma = soma + 20
	elif vet[i]== 4:
		soma = soma + 10
	i = i + 1
	
print(soma)