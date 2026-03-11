from numpy import *

vetor = array(eval(input("valor do vetor: ")))

p = sum(vetor)
print(p)

qtd = 0
for i in range(size(vetor)):
	if (vetor[i] >= 5):
		qtd = qtd + 1
print(qtd)
	
	