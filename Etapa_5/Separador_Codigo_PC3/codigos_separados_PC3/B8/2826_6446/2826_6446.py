from numpy import *
notas = array(eval(input()))
for x in range(size(notas)):
	if notas[x]> 8:
		notas[x] += (10-notas[x])
	elif notas[x] <2:
		notas[x] -= notas[x]
print(notas)