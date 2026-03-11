from numpy import *

v = array(eval(input()))
soma = 0

for i in range(size(v)):
	if(v[i] != 88):
		soma = soma + v[i]
	else:
		soma = (soma) / 2
		
print(soma)

