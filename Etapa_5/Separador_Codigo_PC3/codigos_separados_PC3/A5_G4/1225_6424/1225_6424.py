from numpy import * 
from math import sqrt
from math import pow
v = array(eval(input()))
k = 0
soma = 0
cima = 0
for c in range(size(v)):
	soma = soma + v[c]
	k += 1
m = soma/k
for x in range(size(v)):
	cima = (v[x] - m)**2 + cima
d = sqrt(cima/(size(v)-1))
print(round(d,3))