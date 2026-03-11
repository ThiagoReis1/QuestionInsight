from numpy import *

v = array(eval(input("v ")))
soma = 0

for i in range(size(v)):
	if v[i] == 0:
		soma = 0
		i = i + 1
	else:
		soma = soma + v[i]
		i = i + 1
print(soma)