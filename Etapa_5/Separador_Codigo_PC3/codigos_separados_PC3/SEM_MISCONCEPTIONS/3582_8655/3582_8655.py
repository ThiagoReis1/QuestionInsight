from numpy import *

valores = array(eval(input("")))
soma = 0
for i in range(size(valores)):
	if valores[i] > 160:
		soma = soma - 25 + valores[i]
	else:
		soma = soma + valores[i]

print(round(soma , 2))
	