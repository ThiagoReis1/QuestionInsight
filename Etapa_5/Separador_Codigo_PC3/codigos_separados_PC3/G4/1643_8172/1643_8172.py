from numpy import *

notas = array(eval(input()))
n = 0
j = 0

for i in range(size(notas)):
	if notas[i] >= 5:
		n += 1
print(n)

v = zeros(n, dtype=int)

for i in range(size(notas)):
	if notas[i] >= 5:
		v[j] = i
		j+=1
		
print(v)
		