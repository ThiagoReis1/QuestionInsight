from numpy import *

v = array(eval(input("Digite: ")))

ponto = 10000
i = 0

while i < size(v):
	if v[i] == 1:
		ponto = ponto * 2
	elif v[i] == 2:
		ponto = ponto 
	elif v[i] == 3:
		ponto = ponto / 2
	elif v[i] == 4:
		ponto = ponto / 4
	i = i + 1
print(round(ponto, 2))