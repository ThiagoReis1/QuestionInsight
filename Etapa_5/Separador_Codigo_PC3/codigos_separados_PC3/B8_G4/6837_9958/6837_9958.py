from numpy import *

v = input("sequencia")
i=0
soma = 0
while i < len(v):
	if v[i] == "I":
		soma = soma + 3.75
	elif v[i] == "M":
		soma = soma + 4.5
	elif v[i] == "S":
		soma = soma + 2.9
	i = i+1
soma = round(soma,2)
print(soma)
		