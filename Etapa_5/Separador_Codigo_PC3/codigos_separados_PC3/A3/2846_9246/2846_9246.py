from numpy import *

entrada = input("digite:").split(",")
numeros = zeros(0, dtype=int)


for i in numeros:
	if numeros[i] == 0:
		numeros[i] = 9
	else:
		numeros[i] = 7
print(numeros)