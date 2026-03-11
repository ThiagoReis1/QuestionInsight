from numpy import*

turmas = array(eval(input(": ")))
cont = 0

for i in range (size(turmas)):
	if turmas[i] % 2 == 0:
		cont = cont + 1
print(cont)

indices = zeros(cont, dtype = int)
j = 0

for i in range( size(turmas)):
	if turmas[i] % 2 == 0:
		indices[j] = i
		j = j + 1
print(indices)