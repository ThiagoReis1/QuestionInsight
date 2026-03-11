from numpy import *

numeros = array(eval(input()))

for i in range(size(numeros)):
	if(numeros[i] < 9):
		numeros[i] += 1
	else:
		numeros[i] = 0
		
print(numeros)