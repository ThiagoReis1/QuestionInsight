from numpy import *

numero = array(eval(input("Quais os valores?: ")))

i = 0
soma = 0

while i < size(numero):
	if numero[i] != 0:
		soma = soma + numero[i]
	
	else:
		soma = 0
	
	i += 1
	
print(soma)
	
	