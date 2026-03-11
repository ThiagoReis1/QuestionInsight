from numpy import *

vetor1 = array(eval(input("Entre com o vetor: ")))
vetor2 = array(eval(input("Entre com o vetor: ")))	

i = 0
a = 60
QUENTE = 90
MORNO = 45
FRIO = 0

while (i < size(vetor1)):
	if (vetor[i] == QUENTE):
		custototal = a + 0.005
	elif (vetor[i] == MORNO):
		custototal = a + 0.005
		i = i + 1
	else:
		custototal = a + 0.005
		
print(round(custototal, 2))