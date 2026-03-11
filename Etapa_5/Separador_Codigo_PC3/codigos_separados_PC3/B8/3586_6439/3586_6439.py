from numpy import *

vetor = array(eval(input('Entre com um vetor: ')))

cont = 0
acum = 0

while (cont < size(vetor)):
	if vetor[cont] == 1:
		acum = acum + 100
	elif vetor[cont] == 2:
		acum = acum + 60
	elif vetor[cont] == 3:
		acum = acum + 20
	cont = cont + 1

print(acum)


