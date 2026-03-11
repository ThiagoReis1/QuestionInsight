from numpy import *

v = array(eval(input('Digite os valores; ')))

ponto = 0
i = 0

while i < size(v):
	if v[i] == 1:
		ponto = ponto + 80
	elif v[i] == 2:
		ponto = ponto + 40
	elif v[i] == 3:
		ponto = ponto + 20
	elif v[i] == 4:
		ponto = ponto + 10
	i = i + 1
print(ponto)