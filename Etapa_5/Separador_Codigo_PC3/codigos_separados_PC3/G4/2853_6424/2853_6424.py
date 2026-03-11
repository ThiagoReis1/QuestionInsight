from numpy import *
v = array(eval(input()))
soma = 0
for c in range(size(v)):
	if v[c] != 10:
		soma = soma + v[c]
	else:
		soma = soma * 10
print(soma)