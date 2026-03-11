from numpy import *

v = array(eval(input("")))

soma = 0

for i in range(size(v)):
	if v[i] == 10:
		soma = soma * 10
	elif v[i] != 10:
		soma = soma + v[i] 
print(soma)
