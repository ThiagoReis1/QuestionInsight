# Universidade Federal do Amazonas
# Introdução a ciencia dos computadores
# Avaliacao 05  -  Allan Bezerra 225538

from numpy import *
vetor = array(eval(input("Digite os pesos levantados: ")))
i = 0
k = 0
recorde = 307
while(i < size(vetor)):
	if(vetor[i]>recorde):
		k = k + 1
	i = i + 1
print(recorde)
print(k)
