from numpy import *

turmas = array(eval(input("insira o vetor: ")))

npares = 0


for i in range (0, size(turmas)):
	if (turmas[i] % 2 == 0):
		npares = npares + 1
vet_turmas = zeros(npares, dtype=int)
cont_par = 0 

for x in range (0, size(turmas)):
	if turmas[x] % 2 == 0:
		vet_turmas[cont_par] = x
		cont_par = cont_par + 1

print(npares)
print(vet_turmas)
	
	
