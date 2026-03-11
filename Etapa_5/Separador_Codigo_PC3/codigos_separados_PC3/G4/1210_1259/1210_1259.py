#Julia Caroline
#11 de Agosto de 2016
#Avaliacao 05 Ex1

from numpy import*
#le o vetor
vet = array(eval(input("distancias: ")), dtype = float)
#variaveis de controle
i = 0
cont = 0
#recorde
record = 74.08
#verificacao do vetor
while(i < size(vet)):
	if(vet[i] < record):
		cont = cont + 1
	i = i + 1
print(round(record,2))
print(cont)

