from numpy import *

lista = array(eval(input()))
numeros = zeros(37, dtype=int)

for num in lista:
	numeros[num] = numeros[num] + 1

print(numeros)
