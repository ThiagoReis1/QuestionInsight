from numpy import *

v = array(eval(input("vetor de custos: ")))
soma = 0
for i in range(size(v)):
	if v[i] > 50: 
		soma = soma + (v[i] - v[i] * 8 / 100)
	else:
		soma = soma + v[i]
print(round(soma, 2))