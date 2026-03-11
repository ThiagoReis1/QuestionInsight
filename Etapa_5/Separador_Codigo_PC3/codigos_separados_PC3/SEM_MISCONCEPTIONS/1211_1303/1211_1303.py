#Johnathan Dias				#Matricula:21651445
from numpy import*
vet=array(eval(input("digite os valores dos pesos:")))
record = 307
baixo = 0
i=0
while (i<size(vet)):
	if(vet[i]>record):
		baixo = baixo + 1
	i = i + 1
print(record)
print(baixo)