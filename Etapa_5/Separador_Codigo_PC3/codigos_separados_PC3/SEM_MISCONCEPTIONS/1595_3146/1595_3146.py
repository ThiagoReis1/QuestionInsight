from numpy import *

notas = array(eval(input("Notas: ")))
i = 0 
cont = 0 # Acumula notas acima de 8
# Percorre vetor, indice por indice
while (i < size(notas)):
# Verifica se aluno estah dispensado
if notas[i] >= 8:
cont = cont + 1
i = i + 1
print(cont)