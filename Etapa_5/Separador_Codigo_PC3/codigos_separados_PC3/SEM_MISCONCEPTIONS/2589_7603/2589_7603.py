from numpy import *

vetor = array(eval(input("")))

#vetor[0] = valor minimo
#demais valores = vitimas nao fatais
acum = 0 #qtd de vias que precisam de redutores



for i in range(1, size(vetor)):
	if vetor[i] >= vetor[0]:
		acum = acum + 1
		print(i)
	
	
print(acum) 






