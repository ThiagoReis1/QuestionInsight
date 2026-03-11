from numpy import *

sorteados = array(eval(input()))
numeros = zeros(37,dtype=int)

for i in range(size(sorteados)):
	numeros[sorteados[i]]=numeros[sorteados[i]]+1
	
print(numeros)