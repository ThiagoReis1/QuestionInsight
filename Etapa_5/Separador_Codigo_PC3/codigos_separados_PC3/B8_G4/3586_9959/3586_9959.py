from numpy import*

vet = array(eval(input()))
i=0
soma=0

while i < len(vet):
	if vet[i] ==1:
		soma= soma + 100
	elif vet[i] == 2:
		soma = soma + 60
	elif vet[i] == 3:
		soma = soma + 20
	elif vet[i] == 4:
		soma == soma
	i = i + 1


print(soma)
