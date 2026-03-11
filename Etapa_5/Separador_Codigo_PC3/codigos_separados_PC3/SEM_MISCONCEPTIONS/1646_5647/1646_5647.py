from numpy import *

v = array(eval(input('Valores dos saques efetuados: ')))

quant = 0
for i in range(size(v)):
	if (v[i] <= 50):
		quant = quant + 1

v0 = zeros(quant,dtype=int)
posicao = 0
for i in range(size(v)):
	if (v[i] <= 50):
		v0[posicao] = i
		posicao = posicao + 1
print(quant)
print(v0)