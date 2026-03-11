from numpy import *

v = array(eval(input()))

var = 0
for i in range(size(v)):
	if v[i] >= 5:
		var = var + 1
print(var)
m = zeros(var, dtype=int)

cont = 0
for j in range(size(v)):
	if v[j] >= 5:
		m[cont] = j
		cont = cont + 1
print(m)