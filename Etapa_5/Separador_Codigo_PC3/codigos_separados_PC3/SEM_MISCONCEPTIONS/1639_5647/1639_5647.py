from numpy import *

quant = array(eval(input('Insira a quantidade de alunos: ')))

n = 0
for i in range(size(quant)):
	if (quant[i]%2==0):
		n = n + 1

par = zeros(n, dtype=int)
posicao = 0
for x in range(size(quant)):
	if (quant[x]%2==0):
		par[posicao] = par[posicao] + x
		posicao = posicao + 1
print(n)
print(par)