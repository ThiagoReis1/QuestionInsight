from numpy import *

vet = array(eval(input("Alunos matriculados em cada disciplina: ")))
cond = 0
pum = 0
pdois = 1
ptres = 2

for i in vet:
	if vet[i] % 5 == 0:
		cond = cond + 1
		veti = zeros(cond, dtype=int)
		if vet[i] % 5 == 0:
			veti[i] = veti[i] + vet[i]
		
	
	
print(cond)
print(veti)