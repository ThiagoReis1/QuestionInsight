from numpy import *
v = array(eval(input("Vetor: ")))
i = 0
soma = 10000
while i < size(v):
	if v[i] == 1:
		soma = soma * 2
	elif v[i] == 2:
		soma = soma
	elif v[i] == 3:
		soma = soma / 2
	elif v[i] == 4:
		soma = soma / 4 
	i = i + 1
print(round(soma,2))