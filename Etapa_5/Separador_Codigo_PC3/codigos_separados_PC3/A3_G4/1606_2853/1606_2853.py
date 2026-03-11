from numpy import *

andares = array(eval(input("Insira vetor de paradas: ")))   #andares que o elevador parou

i = 0
soma = 0
prox = 0
ant = 0

while(i < size(andares)):
	prox = andares[i]
	if(andares[i] >= 1 and andares[i] <= 20):
		soma = soma + (andares[i] - 1)
		ant = andares[i]
	if(prox < ant):
		soma = soma + (ant - prox)
	i = i + 1
print(soma)