#---------------------------------------------------------------
# Nome: Ivan Lucas de Oliveira Pacheco
# Data: 13/02/2023
# Objetivo: Contar e listar as turmas com grupos de 5 alunos
#---------------------------------------------------------------
from numpy import*

vet = array(eval(input("Defina o vetor de turmas: ")))

div = 0
for i in range(size(vet)):
	if (vet[i] % 5) == 0:
		div = div + 1
		
indices = arange(div)
var = 0
for j in range(size(vet)):
	if (vet[j] % 5) == 0:
		indices[var] = j
		var = var + 1
		
print (div)
print (indices)