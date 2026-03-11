#Campeonato de Arco e Flecha Diferente

from numpy import *

acertos = array(eval(input("Escreva os aneis que voce acertou: ")))

#Condicao while vetor

i = 0
j = 10000

while (i < size(acertos)):
	if (acertos[i] == 1):
		j = j*2
	elif (acertos[i] == 2):
		j = j
	elif (acertos[i] == 3):
		j = j/2
	elif (acertos[i] == 4):
		j = j/4
	i = i + 1
	
print(j)