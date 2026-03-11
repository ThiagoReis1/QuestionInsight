#Reprovados

from numpy import *

notas = array(eval(input("notas: ")))

aux = 0

for i in range(size(notas)):
	if(notas[i] < 5):
		aux = aux + 1
		
saida = zeros(aux, dtype=int)
aux1 = 0
for i in range(size(notas)):
	if(notas[i] < 5):
		saida[aux1] = i
		aux1 = aux1 + 1
print(aux)
print(saida)
		