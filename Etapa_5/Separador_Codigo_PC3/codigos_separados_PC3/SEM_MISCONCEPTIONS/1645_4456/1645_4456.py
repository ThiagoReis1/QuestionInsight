from numpy import *

vetor = eval(input())

contador = 0

for i in vetor:
	if i >= 2000:
		contador +=1

vetor_acima = zeros(contador,dtype=int)

indice = 0
for i in range(size(vetor)):
	if vetor[i] >= 2000:
		vetor_acima[indice] = i
		indice += 1
print(contador)
print(vetor_acima)