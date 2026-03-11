from numpy import *

vet = array(eval(input('Insira o vetor: ')))

vet0 = zeros(size(vet), dtype=int)
posicao = 0
for i in range(size(vet)):
	vet0[posicao] = vet0[posicao] + (vet[i]**2)
	posicao = posicao + 1
print(vet0)