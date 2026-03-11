from numpy import *

lista = array(eval(input("Valor de vetores: ")))
SOMA = 0
for i in lista:
	if (i == 88):
		SOMA = SOMA/2
	else:
		SOMA = SOMA + i
print(SOMA)