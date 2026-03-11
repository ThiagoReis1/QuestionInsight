from numpy import *

turmas = array(eval(input('')))
grupos = 0

for i in range(size(turmas)):
	if turmas[i] % 5 == 0:
		grupos +=1

ind = zeros(grupos, dtype=int)
print(grupos)
j = 0
for i in range(size(turmas)):
	if turmas[i] % 5 == 0:
		ind[j] = i
		j += 1
print(ind)