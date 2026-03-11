from numpy import *

v = array(eval(input()))
soma = 0

for i in range(size(v)):
	if(v[i]!=99):
		soma += v[i]
	else:
		soma *=2
print(soma)