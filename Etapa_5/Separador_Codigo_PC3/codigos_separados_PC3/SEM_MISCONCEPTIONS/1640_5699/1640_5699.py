from numpy import *

vetor = array(eval(input()))

impares = 0
for i in range(size(vetor)):
	if vetor[i]%2 != 0:
		impares += 1

print(impares)
resultado = zeros(impares,dtype=int)

cont = 0
for i in range(size(vetor)):
	if vetor[i]%2 != 0:
		resultado[cont] = i
		cont += 1

print(resultado)