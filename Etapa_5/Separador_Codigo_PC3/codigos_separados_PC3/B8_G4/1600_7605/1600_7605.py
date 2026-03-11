from numpy import *
v = array(eval(input("vetor: ")))
i = 0
soma = 0
while i < size(v):
	if v[i] < 80:
		soma = soma + v[i]
	elif v[i] > 80:
		soma = soma + (v[i] - (0.15 * v[i]))
	i = i + 1 
print(round(soma,2))
