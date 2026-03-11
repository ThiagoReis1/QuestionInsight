from numpy import *
turmas = array(eval(input("inisira as turmas: ")))
cont = 0
for i in range(size(turmas)):
	if turmas[i] % 5 == 0:
		cont += 1
print(cont)
turmas_5 = zeros(cont, dtype = int)
j = 0
for i in range(size(turmas)):
	if turmas[i] % 5 == 0:
		turmas_5[j] = i
		j += 1
print(turmas_5)
		