#-----------------------------------------------
# Nome: Ivan Lucas de Oliveira Pacheco
# Data: 13/02/2023
# objetivo: Efetuar a soma dos elementos de um vetor dividindo-o quando um numero sinalizador for encontrado
#-----------------------------------------------
from numpy import*

vet = array(eval(input("Defina o vetor: ")))

soma = 0
for i in vet:
	if i != 88:
		soma = soma + i
	else:
		soma = soma / 2
print (soma)