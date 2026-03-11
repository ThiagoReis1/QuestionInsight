from numpy import *

turmas = array(eval(input('insira a lista de turmas: ')))
acm = 0

for i in range(size(turmas)):
	if turmas[i] % 3 == 0:
		acm += 1
ind = zeros(acm, dtype= int)
print(acm)

j = 0

for i in range(size(turmas)):
	if turmas[i] % 3 == 0:
		ind[j] = i
		j += 1

print(ind)