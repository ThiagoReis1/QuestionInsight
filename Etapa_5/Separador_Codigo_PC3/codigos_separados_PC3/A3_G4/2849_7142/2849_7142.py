from numpy import *

v = array(eval(input()))
soma = 0
p = 0

for i in range(size(v)):
	if((v[i]) == 0):
		p = 0
	else:
		p = p + v[i]
print(p)