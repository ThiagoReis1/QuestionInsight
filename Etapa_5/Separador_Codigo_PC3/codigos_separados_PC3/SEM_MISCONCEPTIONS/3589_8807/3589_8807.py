from numpy import *

numeros = array(eval(input("Digite o numero")))
i = 0
soma = 0

while i < size(numeros):
	if numeros[i] == 1:
		soma += 80
	elif numeros[i] == 2:
		soma += 40
	elif numeros[i] == 3:
		soma += 20
	else:
		soma += 10
	i += 1
	total = soma
print(total)