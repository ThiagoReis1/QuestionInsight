from numpy import *

turmas = array(eval(input()))
qtdTurmas = size(turmas)
indices = []
trios = 0

for i in range(qtdTurmas):
	if(turmas[i] % 3 == 0):
		trios += 1
		indices.append(i)
		
indices = array(indices)
print(trios)
print(indices)