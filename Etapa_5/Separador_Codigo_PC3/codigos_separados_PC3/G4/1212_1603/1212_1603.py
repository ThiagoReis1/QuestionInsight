from numpy import *

v = array(eval(input("digite os pesos de levantamento: ")))

i = 0
soma = 0
r = 307

while (i < size(v)):
	if (v[i] < r):
		soma = soma + 1
	i = i + 1
print(r)
print(soma)