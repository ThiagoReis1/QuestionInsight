from numpy import *

v = array(eval(input('Insira o vetor: ')))

v0 = zeros(size(v), dtype=int)
posicao = -1
for i in range(size(v)):
	v0[posicao] = v[-i]
	posicao = posicao + 1
print(v0)
	