from numpy import*
from numpy.linalg import*

vetor = array(eval(input("vetor compra: ")))

cont = 0
for i in range(shape(vetor)[0]):
	if(vetor[i] > 80.0):
		cont = cont + vetor[i] - 5
	else:
		cont = cont + vetor[i]

print(round(cont, 2))